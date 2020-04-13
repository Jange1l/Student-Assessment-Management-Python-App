from django.shortcuts import render, redirect
from registration.models import Course


# All Assessments Page
def all_assessments(request):
    return render(request, 'eval_professor/all-assessments.html')


# Create New Assessment Page
def create_new_assessment(request):
    return render(request, 'eval_professor/create-new-assessment.html')


# My Courses Page
def my_courses(request):
    return render(request, 'eval_professor/my-courses.html')


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

    if semester == 'Fall':
        semester_initial = 'F'
    else:
        semester_initial = 'S'
  
    course = Course(
                    course_name = course_name, 
                    course_code = course_code, 
                    section_number = section_number, 
                    year = year, 
                    semester = semester_initial
                    )
    course.save()
    print("Create Course Success")
    return redirect('/professor-dashboard')