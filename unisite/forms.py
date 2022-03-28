from django import forms
from .models import *


class NewStudent(forms.ModelForm):

    class Meta:
        model = Students
        fields = ['FullName' , 'ID', 'MobNumber' , 'Email' , 'Birthday' , 'Gender' , 'Address']