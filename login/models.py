from django import forms
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class CreateNewUser(forms.ModelForm):
    """
    this class is used to create a new user in the database with the following fields
    """
    class Meta:
        model = User
        fields = ['username', 'password', 'password', 'email', 'first_name', 'last_name']