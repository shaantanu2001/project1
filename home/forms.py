from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.forms import widgets
from django import forms
from home.models import CustomUser
from django.contrib.auth.models import User 

class StudentForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        exclude = ('id',)
        widgets = {
                'dob': widgets.DateInput(attrs={'type':'date','class': 'myfieldclass form-control'})
         }

class Userform(forms.ModelForm):
    class Meta:
        model = User
        phone = forms.CharField(max_length=10)
        exclude = {'is_active','is_staff', 'user_permissions', 'groups', 'is_superuser' ,'last_login', "date_joined"}