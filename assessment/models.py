from django.db import models

# models from other Apps
from account.models import User
from registration.models import Course


class Assessment(models.Model):
    name = models.CharField("assessment name", max_length=255, unique=True)
    description = models.TextField("description", max_length=512, blank=True)

    date_created = models.DateTimeField("date created", auto_now_add=True)

    start_date = models.DateField("start date")
    end_date = models.DateField("end date")

    course = models.ForeignKey(Course, on_delete=models.CASCADE) # the course that this peer review belongs to 
    evaluator = models.ForeignKey(User, related_name="evaluator", on_delete=models.CASCADE) # the person who evaluates others
    team_member = models.ForeignKey(User, related_name="team_member", on_delete=models.CASCADE) # the person being evaluated



class Question(models.Model):
    TYPE_QUESTION_TEXT = 'Text'
    TYPE_QUESTION_MULTIPLE_CHOICE = 'Multiple Choice'

    TYPE_QUESTION = (
        (TYPE_QUESTION_TEXT, "Text"),
        (TYPE_QUESTION_MULTIPLE_CHOICE, "Multiple Choice"),
    )

    # With this assessment foreign key, you can access
    # all questions associated with an assessment using survey.questions.all()
    assessment = models.ForeignKey(Assessment, null=True, related_name="questions", on_delete=models.CASCADE)

    type_question = models.CharField(max_length=255, choices=TYPE_QUESTION, default=TYPE_QUESTION_MULTIPLE_CHOICE)
    # This way its easier to check for the question type, when ever you need to.
    # E.g. question.type_question == Question.TYPE_QUESTION_TEXT


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name="question_choices", on_delete=models.CASCADE)
    choice_text = models.CharField("choice text", max_length=200)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    student = models.ForeignKey(User, related_name="student", on_delete=models.CASCADE) # the person who evaluates others
    answer_text = models.CharField("answer text", max_length=512, null=True)
    date_added = models.DateTimeField("date added", auto_now_add=True)
    date_modified = models.DateTimeField("date modified", auto_now=True)