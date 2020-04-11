from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.utils.translation import ugettext as _


# Home Page
def index(request):
    return render(request, 'login/index.html')


# Student Login Page
def student_login(request):
    return render(request, 'login/student-login.html')


# Instructor Login Page
def professor_login(request):
    return render(request, 'login/professor-login.html')


# Student Dashboard Page
def student_dashboard(request):
    return render(request, 'login/student-dashboard.html')


# Instructor Dashboard Page
def professor_dashboard(request):
    return render(request, 'login/professor-dashboard.html')


# *************************** LOGIN ***************************
def log_in(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, email=email, password=password)

    # WRONG EMAIL OR PASSWORD
    if user == None:
        messages.error(request, 'You entered your email or password incorrectly.')
        if request.META['HTTP_REFERER'].endswith('student-login'):
            return redirect('/student-login')
        elif request.META['HTTP_REFERER'].endswith('professor-login'):
            return redirect('/professor-login')

    # PASSED USER VALIDATION
    else:
        # ---------------STUDENT------------------------------------------ 
        if user.is_student == True and user.is_instructor != True:
            # EXCEPTION: if this student is logging in on the professor-login
            if request.META['HTTP_REFERER'].endswith('professor-login'):
                messages.error(request, 'Students must login from the student login page.')
                return redirect('/student-login')
            # NORMAL CASE: student logs in on student-login
            elif request.META['HTTP_REFERER'].endswith('student-login'):
                login(request, user)
                return redirect('/student-dashboard')
            # WRONG EMAIL OR PASSWORD
            else:
                messages.error(request, 'You entered your email or password incorrectly.')
                return redirect('/student-login')

        # ---------------INSTRUCTOR---------------------------------------
        elif user.is_instructor == True and user.is_student != True:
            # EXCEPTION: if this instructor is logging in on the student-login
            if request.META['HTTP_REFERER'].endswith('student-login'):
                messages.error(request, 'Professors must login from the professor login page.')
                return redirect('/professor-login')
            # NORMAL CASE: instructor logs in on professor-login
            elif request.META['HTTP_REFERER'].endswith('professor-login'):
                login(request, user)
                return redirect('/professor-dashboard')
            # WRONG EMAIL OR PASSWORD
            else:
                messages.error(request, 'You entered your email or password incorrectly.')
                return redirect('/professor-login')
    

# *************************** LOGOUT***************************
