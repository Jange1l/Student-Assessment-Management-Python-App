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
    filtered_list = []
    for i in assessment_list:
       if  request.user in i.course.students.all():
           filtered_list.append(i)
        
    context = {
        'assessment_list': filtered_list,
    }
    
    return render(request, 'eval_student/peer-assessments.html', context=context)


# Completed Assessments Page
def completed_assessments(request):
    return render(request, 'eval_student/completed-assessments.html')


# Answer Assessment Page
def answer_assessment(request, assessment_id):
    assessment = Assessment.objects.get(pk=assessment_id) # the assessment object
    questions = assessment.questions.all() # set of questions in this assessment
    teams = Team.objects.filter(course=assessment.course) # set of teams in this course

    # Find the list of people who will be evaluated
    evaluated_team = None
    evaluated = []
    for team in teams:
        if request.user in team.student.all():
            evaluated_team = team
            for each in team.student.all():
                if each != request.user:
                    evaluated.append(each)

    context = {
        'assessment': assessment,
        'question_list': questions,
        'team': evaluated_team,
        'evaluated_list': evaluated,
    }
    return render(request, 'eval_student/answer-assessment.html', context=context)