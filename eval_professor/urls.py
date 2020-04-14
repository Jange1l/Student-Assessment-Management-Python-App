from . import views
from django.urls import path
from django.conf.urls import url


urlpatterns = [
    # path for pages
    path('all-assessments', views.all_assessments, name='all-assessments'),
    path('create-new-assessment', views.create_new_assessment, name='create-new-assessment'),
    path('my-courses', views.my_courses, name='my-courses'),
    path('create-new-course', views.create_new_course, name='create-new-course'),
    path('teams-students', views.teams_students, name='teams-students'),
    
    # path for functions
    path('make_new_course', views.make_new_course, name='make_new_course'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),
]