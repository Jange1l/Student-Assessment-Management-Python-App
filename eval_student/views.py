from django.shortcuts import render, redirect


# Peer Assessments Page
def peer_assessments(request):
    return render(request, 'eval_student/peer-assessments.html')

    
# Completed Assessments Page
def completed_assessments(request):
    return render(request, 'eval_student/completed-assessments.html')