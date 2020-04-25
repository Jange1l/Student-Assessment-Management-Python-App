from django.shortcuts import render, redirect

# models imported from other apps
from registration.models import Course, Team
from assessment.models import Assessment, Question, Answer
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


# Submit - on answer assessment page
def submit_assessment(request, assessment_id):
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

    # create answer instances and save to the answer set in assessment
    for student_evaluated in evaluated:
        for question in questions:
            name_for_post = "q_@{}".format(question.id)
            ans = request.POST[name_for_post]

            if question.type_answer == question.TYPE_Rating:
                answer = Answer(
                            question = question,
                            evaluator = request.user,
                            team_member = student_evaluated,
                            answer_text = None,
                            answer_rating = int(ans),
                        )
            else:
                answer = Answer(
                            question = question,
                            evaluator = request.user,
                            team_member = student_evaluated,
                            answer_text = ans,
                            answer_rating = None,
                        )
            answer.save()

            # add the answer to the answer set under this assessment
            assessment.answers.add(answer)
            assessment.save()
 
    # add the current user to the set of users who have completed this assessment
    assessment.completed_students.add(request.user)
    assessment.save()

    return completed_assessments(request)