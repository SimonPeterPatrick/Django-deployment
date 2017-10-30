# -*- coding: utf-8 -*-
from app_base.models import UserProfil
from django.contrib.auth.models import User
from django import forms

class UserProfilForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ('username', 'email', 'password')
    
class UserProfilInfo(forms.ModelForm):   
    class Meta():
        model = UserProfil
        fields = ('portfolio_site','portfolio_pic')
        
        