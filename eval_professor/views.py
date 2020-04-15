from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

# models imported from other apps
from registration.models import Course
from account.models import User


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
    return render(request, 'eval_professor/teams-students.html')



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
    return redirect('my-courses')


# Delete a course
def delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    course.delete()
    messages.error(request, 'Course deleted.')
    print("Course Deleted")
    course_list = Course.objects.all()
    context = {
        'course_list': course_list,
    }
    return render(request, 'eval_professor/my-courses.html', context = context)