from django.db import models

# models from other Apps
from account.models import User


class Assessment(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=512, blank=True)


class Question(models.Model):
    TYPE_QUESTION_TEXT = 'Text'
    TYPE_QUESTION_MULTIPLE_CHOICE = 'Multiple Choice'

    TYPE_QUESTION = (
        (TYPE_QUESTION_TEXT, "Text"),
        (TYPE_QUESTION_MULTIPLE_CHOICE, "Multiple Choice"),
    )

    # With this assessment foreign key, you can access
    # all questions associated with an assessment using survey.questions.all()
    assessment = models.ForeignKey(Assessment, null=True, related_name="questions")
    title = models.CharField(max_length=255)
    type_question = models.CharField(max_length=255, choices=TYPE_QUESTION, default=TYPE_QUESTION_MULTIPLE_CHOICE)
    # This way its easier to check for the question type, when ever you need to.
    # E.g. question.type_question == Question.TYPE_QUESTION_TEXT


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name="question_choices")
    choice_text = models.CharField(max_length=200)


class Answer(models.Model):
    question = models.ForeignKey(Question)
    user = models.ForeignKey(User)
    answer_text = models.CharField(max_length=512, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)