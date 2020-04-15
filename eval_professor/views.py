from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

# models imported from other apps
from registration.models import Course


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