from django.urls import path
from . import views


urlpatterns = [

    path('', views.login, name='login'),
    path('home/', views.page0, name='index0'),
    path('managestudent/', views.page1, name='index1'),
    path('managecourse/', views.page2, name='index2'),
    path('managestaff/', views.page3, name='index3'),
    path('addstudent/', views.page4, name='index4'),
    path('addcourse/', views.page6, name='index6'),
    path('addstaff/', views.page5, name='index5'),
    



]
