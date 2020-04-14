from . import views
from django.urls import path
from django.conf.urls import url


urlpatterns = [
    path('student-dashboard', views.student_dashboard, name='student-dashboard'),
    path('peer-assessments', views.peer_assessments, name='peer-assessments'),
    path('completed-assessments', views.completed_assessments, name='completed-assessments'),
    
]