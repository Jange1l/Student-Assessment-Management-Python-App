from django.db import models

# models from other Apps
from account.models import User
from registration.models import Course

# python packages
import datetime


class Question(models.Model):
    TYPE_TEXT = 'Text'
    TYPE_Rating = 'Rating'

    ANSWER_TYPE = (
        (TYPE_TEXT, "Text"),
        (TYPE_Rating, "Rating"),
    )

    question_text = models.CharField(max_length=500)
    type_answer = models.CharField(max_length=6, choices=ANSWER_TYPE, default=TYPE_Rating)
    # This way its easier to check for the question type, when ever you need to.
    # E.g. question.type_question == Question.TYPE_QUESTION_TEXT

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    evaluator = models.ForeignKey(User, related_name="evaluator", on_delete=models.CASCADE) # the person who evaluates others
    team_member = models.ForeignKey(User, related_name="team_member", on_delete=models.CASCADE) # the person being evaluated

    answer_text = models.CharField("answer text", max_length=512, null=True) # answer for free response
    answer_rating = models.SmallIntegerField("answer rating", null=True) # answer for rating question (1-5)

    date_added = models.DateTimeField("date added", auto_now_add=True)
    date_modified = models.DateTimeField("date modified", auto_now=True)

    def __str__(self):
        return "Answer #{}".format(self.id)

    def get_answer(self):
        if self.question.type_answer == self.question.TYPE_Rating:
            return self.answer_rating
        else:
            return self.answer_text


class Assessment(models.Model):
    name = models.CharField("assessment name", max_length=255)
    description = models.TextField("description", max_length=512, blank=True)

    date_created = models.DateTimeField("date created", auto_now_add=True)

    start_date = models.DateField("start date")
    end_date = models.DateField("end date")

    course = models.ForeignKey(Course, on_delete=models.CASCADE) # the course that this peer review belongs to 

    questions = models.ManyToManyField(Question) # a set of Questions under this assessment

    answers = models.ManyToManyField(Answer) # a set of Answers under this assessment

    completed_students = models.ManyToManyField(User, related_name="completed_students") # a set of Users who have completed this assessment

    def __str__(self):
        return "{} for {}".format(self.name, self.course.course_name)

    def is_current(self):
        "Returns whether the assessment end date is within 60 days."
        if self.end_date + datetime.timedelta(days=60) > datetime.datetime.now().date(): # end date + 60 >= current date
            return True
        return False

    def time_left(self):
        time = str(self.end_date - datetime.datetime.now().date())
        return time[:time.find(',')]

    def is_missed(self):
        time = str(self.end_date - datetime.datetime.now().date())
        if time[0] == '-':
            return True
        return False



class Choice(models.Model):
    question = models.ForeignKey(Question, related_name="question_choices", on_delete=models.CASCADE)
    choice_text = models.CharField("choice text", max_length=200)

