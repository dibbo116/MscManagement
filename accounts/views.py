from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *
from django.contrib.auth.hashers import make_password, check_password
from django.urls import reverse
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        phn = request.POST.get('phone_no1', None)
        gender = request.POST.get('gender', None)
        dept = request.POST.get('department_id', None)
        roll = request.POST.get('roll_no', None)
        reg_no = request.POST.get('registration_no', None)
        add_year = request.POST.get('admission_year', None)
        cur_year = request.POST.get('current_year', None)
        sems = request.POST.get('current_semester', None)
        pass1 = request.POST.get('password1', None)
        pass2 = request.POST.get('password2', None)

        if pass1 == pass2:
            #alredy registed check
            username = 'RUET'+roll
            pass2 = make_password(pass2)
            user = User.objects.create_user(username=username, password=pass2)
            user.email = email
            user.first_name = name
            userinfo = StudentInfo.objects.create(user=user, phone=phn, gender=gender, dept=dept,
                roll=roll, reg=reg_no, adm_year=add_year, cur_year=cur_year, sems=sems)
            userinfo.picture = request.FILES.get('propic', None)
            user.save()
            userinfo.save()
            messages.success(request, 'Registration was done successfuly.')
        else:
            print('password do not match')


    return render(request, 'accounts/usersignup.html')


def teachersignup(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        phn = request.POST.get('phone_no1', None)
        gender = request.POST.get('gender', None)
        dept = request.POST.get('department_id', None)
        desig = request.POST.get('designation_id', None)
        pass1 = request.POST.get('password1', None)
        pass2 = request.POST.get('password2', None)

        if pass1 == pass2:
            #alredy registed check
            username = 'RUET'+phn
            pass1 = make_password(pass1)
            user = User.objects.create(first_name=name, username=username, email=email)
            user.set_password(pass1)
            userinfo = TeacherInfo.objects.create(user=user, phone=phn, gender=gender, dept=dept, designation=desig)
            userinfo.picture = request.FILES.get('propic',None)
            user.is_staff = True
            user.save()
            userinfo.save()
            auth.login(request, user)
            messages.success(request, 'Registration was done successfuly.')
        else:
            print('password do not match')

    return render(request, 'accounts/teachersignup.html')


def  Teacherlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)
        passw = request.POST.get('password', None)

        if email is not None and passw is not None:
            user = User.objects.get(email=email)
            if user.is_staff:
                if user.check_password(passw):
                    auth.login(request, user)
                    print('logged in successfuly')
                    return redirect(reverse('home'))
                else:
                    print('Password not match')
                    return redirect(reverse('login'))
            else:
                messages.error(request, 'You are not a Teacher')
    return render(request, 'accounts/Teacherlogin.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)
        passw = request.POST.get('password', None)

        if email is not None and passw is not None:
            user = User.objects.get(email=email)
            if not user.is_staff:
                if user.check_password(passw):
                    auth.login(request, user)
                    print('logged in successfuly')
                    return redirect(reverse('home'))
                else:
                    print('Password not match')
                    return redirect(reverse('login'))
            else:
                messages.error(request, 'You are not a Student')

    return render(request, 'accounts/login.html')

def logout(request):
        auth.logout(request)
        return redirect('home')
