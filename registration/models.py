from django.db import models

# models from other Apps
from account.models import User

# python packages
import datetime


# ------------------------- COURSE MODEL -----------------------------------------
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    index = models.IntegerField("course index", null=True) # can be used in view to create course index
    course_name = models.CharField("course name", max_length=60)
    course_code = models.IntegerField("course code")
    section_number = models.SmallIntegerField("section number")
    year = models.SmallIntegerField("year of realization")
    semester_choices = (
        ('S', 'Spring'),
        ('F', 'Fall'),
    )
    semester = models.CharField("semester of realization", max_length = 1, choices = semester_choices)


    def is_active(self):
        "Returns whether the course is active."
        if self.year >= datetime.datetime.now().year: # realization year >= current year
            if self.semester == 'S':
                month = 6
            else:
                month = 12
            if month >= datetime.datetime.now().month: # realization month >= current month
                return True
        return False




# ------------------------- TEAM MODEL -----------------------------------------
class Team(models.Model):
    
    # Primary Key is the auto-generated IDs
    team_number = models.IntegerField("team number")
    team_name = models.CharField("team name", max_length=60)
    
    course = models.ForeignKey(Course, on_delete = models.CASCADE) # a Course object
    student = models.ForeignKey(User, on_delete = models.CASCADE) # a User object



# ------------------------- TEACHING_CREW MODEL -----------------------------------------
class Teaching_Crew(models.Model):
    """
    This model allows one course to have multiple professors.
    """
    # Primary Key is the auto-generated IDs
    course = models.ForeignKey(Course, on_delete = models.CASCADE) # a Course object
    professor = models.ForeignKey(User, on_delete = models.CASCADE) # a User object
