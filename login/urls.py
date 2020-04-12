from . import views
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('student-login', views.student_login, name='student-login'),
    path('professor-login', views.professor_login, name='professor-login'),
    path('student-dashboard', views.student_dashboard, name='student-dashboard'),
    path('professor-dashboard', views.professor_dashboard, name='professor-dashboard'),
    path('password-reset', views.password_reset, name='password-reset'),

    path('log_in', views.log_in, name='log_in'),
    path('log_out', views.log_out, name='log_out'),
    path('change_password', views.change_password, name='change_password'),
]