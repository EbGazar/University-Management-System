from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Staff(models.Model):

    FullName = models.CharField(max_length=150)
    ID = models.IntegerField(unique=True)
    MobNumber = models.IntegerField()
    Email = models.CharField(max_length=300)
    Birthday = models.IntegerField()
    Gender = models.CharField(max_length=50)
    Address = models.CharField(max_length=300)

    def __str__(self):
        return self.FullName

class Course(models.Model):

    CourseID = models.IntegerField(unique=True)
    CourseName = models.CharField(max_length=150)
    CourseInstructor = models.CharField(max_length=150)
    CreditHours = models.IntegerField()
    RequiredCourse = models.CharField(max_length=150)
    CourseCode = models.CharField(max_length=20,unique=True)

class Students(models.Model):

    FullName = models.CharField(max_length=200)
    ID = models.IntegerField(unique =True)
    MobNumber = models.IntegerField()
    Email = models.CharField(max_length=200)
    Birthday = models.IntegerField()
    Gender = models.CharField(max_length=20)
    Address = models.CharField(max_length=200)

    def __str__(self):
        return self.FullName

