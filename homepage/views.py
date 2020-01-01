from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *
from django.contrib.auth.hashers import make_password, check_password
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def home(request):

    return render(request, 'homepage/home.html')


def admission(request):

    return render(request,'homepage/admission.html')


def course(request):

    return render(request,'homepage/course.html')

def history(request):

    return render(request,'homepage/history.html')
