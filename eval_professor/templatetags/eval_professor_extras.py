from django import template

from registration.models import Course, Team
from assessment.models import Assessment, Question, Result_set
from account.models import User

import numpy as np

register = template.Library()


@register.simple_tag
def get_class_average(course, assessment):
    """Returns the average score of the class"""
    result_set_list = []
    for team in Team.objects.filter(course=course).all():
        for result_set in Result_set.objects.filter(team=team).all():
            if result_set in assessment.result_sets.all(): # check if this result_set is under this assessment
                result_set_list.append(result_set)
    return round(np.mean([result_set.get_overall_average() for result_set in result_set_list]), 2)



@register.simple_tag
def get_team_average(team, assessment):
    """Returns the average score of the team"""
    result_set_list = []
    for result_set in Result_set.objects.filter(team=team).all():
            if result_set in assessment.result_sets.all(): # check if this result_set is under this assessment
                result_set_list.append(result_set)
    return round(np.mean([result_set.get_overall_average() for result_set in result_set_list]), 2)


@register.simple_tag
def find_result_set(result_sets, student, team):
    """Returns the Result_set instance of the given student in the given team"""
    return result_sets.filter(student=student, team=team).first()


@register.simple_tag
def get_per_question_average(result_set, q_id):
        scores = [answer.answer_rating for answer in result_set.rating_answers.all() if answer.question.id == q_id] # a list of scores of that question
        return round(np.mean(scores), 2)
