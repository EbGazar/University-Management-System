from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from unisite.models import *
from django.shortcuts import *
from django.http import *
from django.contrib.auth.models import User

# Create your views here.


def signup(request):

    form = UserCreationForm()

    if request.method == 'POST':

        Name = request.POST['namee']
        Id = request.POST['id']
        email = request.POST['email']
    
        new_student = User

        return redirect('index1')

    return render(request, 'addstudent.html',{'student' : student})


def signup(request):

    form = UserCreationForm()

    if request.method == 'POST':

        Name = request.POST['namee']
        Id = request.POST['id']
        email = request.POST['email']

    
        new_staff = Students.objects.create(FullName = Name[0], ID = Id, Email = email)

        return redirect('index1')

    return render(request, 'addstaff.html',{'student' : student})

