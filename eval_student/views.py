from django.shortcuts import render, redirect

# models imported from other apps
from registration.models import Course, Team
from assessment.models import Assessment, Question, Answer, Result_set
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

    # create result_set instances to store answers
    for each_student in evaluated:
        if len(Result_set.objects.filter(student=each_student, team=evaluated_team)) == 0: # if such Result_set does not exist, create one
            result_set = Result_set(
                                student = each_student,
                                team = evaluated_team,            
                        )
            result_set.save()

    for student_evaluated in evaluated:
        # find the result_set of the student being evaluated
        result_set = Result_set.objects.filter(student=student_evaluated, team=evaluated_team).first()
        for question in questions:
            name_for_post = "q_@{}".format(question.id)
            ans = request.POST[name_for_post]

            # create answer instances 
            if question.type_answer == question.TYPE_Rating:
                answer = Answer(
                            question = question,
                            evaluator = request.user,
                            team_member = student_evaluated,
                            answer_text = None,
                            answer_rating = int(ans),
                        )
                answer.save()
                # add the answer to the Result_set.rating_answers
                result_set.rating_answers.add(answer)
                result_set.save()
            else:
                answer = Answer(
                            question = question,
                            evaluator = request.user,
                            team_member = student_evaluated,
                            answer_text = ans,
                            answer_rating = None,
                        )
                answer.save()
                # add the answer to the Result_set.text_answers
                result_set.text_answers.add(answer)
                result_set.save()
            
        # add the Result_set to this assessment
        assessment.result_sets.add(result_set)
        assessment.save()
 
    # add the current user to the set of users who have completed this assessment
    assessment.completed_students.add(request.user)
    assessment.save()

    return completed_assessments(request)