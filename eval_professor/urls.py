from . import views
from django.urls import path
from django.conf.urls import url


urlpatterns = [
    # path for pages
    path('professor-dashboard', views.professor_dashboard, name='professor-dashboard'),
    path('all-assessments', views.all_assessments, name='all-assessments'),
    path('create-new-assessment', views.create_new_assessment, name='create-new-assessment'),
    path('my-courses', views.my_courses, name='my-courses'),
    path('create-new-course', views.create_new_course, name='create-new-course'),
    path('teams-students', views.teams_students, name='teams-students'),
    
    # path for functions
    # functions for course
    path('make_new_course', views.make_new_course, name='make_new_course'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),
    path('add_student/<int:course_id>/', views.add_student, name='add_student'),
    path('remove_student/<int:course_id>/<str:eagle_id>/', views.remove_student, name='remove_student'),

    # functions for teams
    path('add_new_team', views.add_new_team, name='add_new_team'),
    path('delete_team/<int:team_id>/', views.delete_team, name='delete_team'),
]