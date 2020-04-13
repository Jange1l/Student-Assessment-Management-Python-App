from django.shortcuts import render, redirect


# All Assessments Page
def all_assessments(request):
    return render(request, 'eval_professor/all-assessments.html')


# Create New Assessment Page
def create_new_assessment(request):
    return render(request, 'eval_professor/create-new-assessment.html')

    
# Teams & Students Page
def teams_students(request):
    return render(request, 'eval_professor/teams-students.html')