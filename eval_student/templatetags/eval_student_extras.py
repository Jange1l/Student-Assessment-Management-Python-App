from django import template

from registration.models import Course, Team
from assessment.models import Assessment, Question, Result_set
from account.models import User

import numpy as np

register = template.Library()


@register.simple_tag
def get_eval_list(assessment, current_user):
    """Returns the list of teammates who are evaluated"""
    for team in Team.objects.all():
        if current_user in team.student.all() and team.course == assessment.course: # get the team
            evaluated_list = [student for student in team.student.all() if student != current_user]
    return evaluated_list


@register.simple_tag
def get_answer_list(assessment, student):
    """Returns a list of answers for the student"""
    result_set = assessment.result_sets.filter(student=student).first()
    answer_list = []
    for answer in result_set.rating_answers.all():
        answer_list.append(answer)
    for answer in result_set.text_answers.all():
        answer_list.append(answer)
    return answer_list
    