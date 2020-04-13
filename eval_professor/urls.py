from . import views
from django.urls import path
from django.conf.urls import url


urlpatterns = [
    path('all-assessments', views.all_assessments, name='all-assessments'),
    path('create-new-assessment', views.create_new_assessment, name='create-new-assessment'),
    path('teams-students', views.teams_students, name='teams-students'),
    
]