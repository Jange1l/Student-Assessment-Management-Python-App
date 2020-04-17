from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

# models imported from other apps
from registration.models import Course, Team
from account.models import User

# import Python packages
from re import search as regex_search



# Instructor Dashboard Page
def professor_dashboard(request):
    return render(request, 'eval_professor/professor-dashboard.html')


# All Assessments Page
def all_assessments(request):
    return render(request, 'eval_professor/all-assessments.html')


# Create New Assessment Page
def create_new_assessment(request):
    return render(request, 'eval_professor/create-new-assessment.html')


# My Courses Page
def my_courses(request):
    course_list = Course.objects.all()
    context = {
        'course_list': course_list,
    }
    return render(request, 'eval_professor/my-courses.html', context = context)


# Create New Course Page
def create_new_course(request):
    return render(request, 'eval_professor/create-new-course.html')

    
# Teams & Students Page
def teams_students(request):
    team_list = Team.objects.all().order_by('team_name')
    course_list = Course.objects.all() # this info is needed for the dropdown select in creating new team
    context = {
        'team_list': team_list,
        'course_list': course_list,
    }
    return render(request, 'eval_professor/teams-students.html', context = context)




# ----------------------------------- Course Section (functions below are for courses) --------------

# Function: create a new course
def make_new_course(request):
    course_name = request.POST['course name']
    course_code = request.POST['course code']
    section_number = request.POST['section number']
    year = request.POST['year']
    semester = request.POST['semester']
    co_professor_id = request.POST['co-professor ID']
    # CAN CHANGE THIS TO SELECT CURRENT PROF

    course_name = course_name.title()

    # the professor registering must be the current user
    professor = request.user

    # convert text to required format in the model
    if semester == 'Fall':
        semester_initial = 'F'
    else:
        semester_initial = 'S'
 
    # Validations of input formatting are DONE in html templates

    # Validation to prevent duplicate course
    course_valid = False
    if len(Course.objects.filter(course_code=course_code, 
                            section_number=section_number, 
                            year=year, 
                            semester=semester_initial)) > 0:
        messages.error(request, "Error: You cannot create duplicate courses.")
        return redirect('create-new-course')
    else:
        course_valid = True

    # Validations for co-professor
    co_prof_valid = False
    if co_professor_id != '':
        co_professor = User.objects.filter(eagle_id=co_professor_id).first()
        if co_professor is None:
            messages.error(request, "Error: You incorrectly entered the co-professor's Eagle ID.")
            return redirect('create-new-course')
        elif not co_professor.is_instructor:
            messages.error(request, "Error: The co-professor's Eagle ID you entered is not a professor.")
            return redirect('create-new-course')
        elif co_professor_id == request.user.eagle_id:
            messages.error(request, "Error: The co-professor's Eagle ID cannot be the same as your Eagle ID.")
            return redirect('create-new-course')
        else:
            co_prof_valid = True
  
    if course_valid:
    # Create an instance of course
        course = Course(
                        course_name = course_name, 
                        course_code = course_code, 
                        section_number = section_number, 
                        year = year, 
                        semester = semester_initial,
                        )
        course.save()

    # Add to Many-to-Many field
    course.professors.add(professor)
    if co_prof_valid:
        course.professors.add(co_professor)
    course.save()

    messages.error(request, 'New course creation is successful!')
    print("Create Course Success")
    return my_courses(request)


# Delete a course
def delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    course.delete()
    messages.error(request, 'Course deleted.')
    print("Course Deleted")
    return my_courses(request) # refresh page



def add_student(request, course_id):
    # This is add student to course. There is another function add_student_to_team
    id_or_email = request.POST['id or email']
    eagle_id = ''
    email = ''
    valid_student = False
    # check is it email format
    if regex_search(r'@bc.edu', id_or_email) is not None:  
        email = id_or_email  
    # check is it eagle id format       
    elif id_or_email.isdigit() and len(id_or_email) == 8:
        eagle_id = id_or_email
    else:
        messages.error(request, "Error: The format of email or Eagle ID is incorrect.")
    
    # get course object
    course = get_object_or_404(Course, pk=course_id)

    # Validate the existance of the student
    if eagle_id != '':
        new_student = User.objects.filter(eagle_id = eagle_id).first()
        valid_student = True
    elif email != '':
        new_student = User.objects.filter(email = email).first()
        valid_student =True
    else:
        messages.error(request, "Error: Student is not found.")
    
    if valid_student:
        course.students.add(new_student)
        course.save()
        print("student successfully added")

    return my_courses(request) # refresh page



def remove_student(request, course_id, eagle_id):
    course = Course.objects.get(pk=course_id)
    student = User.objects.get(eagle_id=eagle_id)
    course.students.remove(student)
    course.save()
    messages.error(request, "Student removed.")
    return my_courses(request) # refresh page



# ----------------------------------- Team Section (functions below are for teams) --------------
def add_new_team(request):
    team_name = request.POST['team name']
    course_id = request.POST['course id']

    # Cap the first letter
    team_name = team_name[0].upper() + team_name[1:]

    # Validations
    team_valid = False

    # Check for duplicate names
    if len(Team.objects.filter(team_name=team_name)) > 0:
         messages.error(request, "Error: The team name you entered has already been taken.")

    else:
        team_valid = True

    # Create an instance of team
    if team_valid:
        team = Team(
                    team_name = team_name, 
                    course = Course.objects.filter(id=course_id).first(), 
                    )
        team.save()

    return teams_students(request) # refresh page


# Delete a team
def delete_team(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    team.delete()
    messages.error(request, 'Team deleted.')
    return teams_students(request) # refresh page


# Add a student to a team
def add_student_to_team(request, team_id):
    name_id = request.POST['name_id']
    eagle_id = name_id[-8:]
    
    valid_student = False
    
    # get team object
    team = get_object_or_404(Team, pk=team_id)

    # Validate the existance of the student
    if eagle_id != '':
        new_student = User.objects.filter(eagle_id = eagle_id).first()
        valid_student = True
    else:
        messages.error(request, "Error: Student is not found.")

    # Validate if the student is in the course
    if valid_student:
        if new_student not in team.course.students.all():
            messages.error(request, "Error: The student is not in this course")
            valid_student = False

    # Validate if the student is already in another team
    if valid_student:
        course = team.course # the course object
        team_list = Team.objects.filter(course=course) # list of teams in this course
        for team in team_list:
            if len(team.student.filter(eagle_id=eagle_id)) > 0:
                messages.error(request, "Error: This student is already in a team ({})".format(team.team_name))
                valid_student = False
    
    if valid_student:
        team.student.add(new_student)
        team.save()

    return teams_students(request) # refresh page


# remove a student from a team
def remove_student_from_team(request, team_id, eagle_id):
    team = Team.objects.get(pk=team_id)
    student = User.objects.get(eagle_id=eagle_id)
    team.student.remove(student)
    team.save()
    messages.error(request, "Student removed.")
    return teams_students(request) # refresh page