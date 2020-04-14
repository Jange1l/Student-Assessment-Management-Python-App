from django.shortcuts import render, redirect


# Student Dashboard Page
def student_dashboard(request):
    return render(request, 'eval_student/student-dashboard.html')


# Peer Assessments Page
def peer_assessments(request):
    return render(request, 'eval_student/peer-assessments.html')

    
# Completed Assessments Page
def completed_assessments(request):
    return render(request, 'eval_student/completed-assessments.html')