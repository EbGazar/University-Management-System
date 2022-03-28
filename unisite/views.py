from django.shortcuts import *
from django.http import *
from .models import *
# Create your views here.


def login(request):

    return render(request, "proj.html")


def page1(request,redirect_field_name=None):

    student = Students.objects.all()
    return render(request, 'Managestudent.html', {'student': student})



def page2(request):

    course = Course.objects.all()
    return render(request, 'Managecourse.html', {'course': course})


def page3(request):

    staff = Staff.objects.all()
    return render(request, 'Managestaff.html', {'staff': staff})


def page4(request):

    student = Students.objects.all()

    if request.method == 'POST':

        Name = request.POST['namee']
        Id = request.POST['id']
        mobile = request.POST['mobo']
        email = request.POST['email']
        birthday = request.POST['birthday']
        gender = request.POST['gender']
        address = request.POST['address']
    
        new_student = Students.objects.create(FullName = Name, ID = Id , MobNumber = mobile , Email = email , Birthday = birthday , Gender = gender, Address= address)
        return redirect('index1')

    return render(request, 'addstudent.html',{'student' : student})

def page5(request):

    staff = Staff.objects.all()

    if request.method == 'POST':

        name = request.POST['namee']
        Id = request.POST['id']
        mobile = request.POST['mobo']
        email = request.POST['email']
        birthday = request.POST['birthday']
        gender = request.POST['gender']
        address = request.POST['address']

        new_staff = Staff.objects.create(
            FullName=name, ID=Id, MobNumber=mobile, Email=email, Birthday=birthday, Gender=gender, Address=address)
        return redirect('index5')

    return render(request, 'addstaff.html',{'staff' : staff})


def page6(request):
    course = Course.objects.all()

    if request.method == 'POST':

        Name = request.POST['NAME']
        Id = request.POST['ID']
        instructor = request.POST['INS']
        NumOfHou = request.POST['NOH']
        ReqCourse = request.POST['ARC']
        code = request.POST['code']

        new_course = Course.objects.create(
            CourseName=Name, CourseID=Id, CourseInstructor=instructor, CreditHours=NumOfHou, RequiredCourse=ReqCourse, CourseCode=code)
        return redirect('index6')
    return render(request, 'addcourse.html', {'course': course})


def page0(request):
    tot_students = Students.objects.count()
    tot_staff = Staff.objects.count()
    return render(request, 'home.html',{'total_students': tot_students,'total_staff' : tot_staff})