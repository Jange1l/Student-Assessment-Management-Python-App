from django.shortcuts import render, redirect

# models imported from other apps
from registration.models import Course, Team
from assessment.models import Assessment, Question
from account.models import User

# import Python packages
from re import search as regex_search
import datetime

# Student Dashboard Page
def student_dashboard(request):
    return render(request, 'eval_student/student-dashboard.html')


# Peer Assessments Page
def peer_assessments(request):
    assessment_list = Assessment.objects.all()
    context = {
        'assessment_list': assessment_list,
    }
    # for i in assessment_list:
    #     print(i.name, i.end_date, i.questions)
    return render(request, 'eval_student/peer-assessments.html', context = context)

    
# Completed Assessments Page
def completed_assessments(request):
    return render(request, 'eval_student/completed-assessments.html')