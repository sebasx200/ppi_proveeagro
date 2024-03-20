# this file is created to create forms for login app
from django import forms
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User

class CreateNewUser(UserCreationForm):
    """
    this class is created to create the form for the sign up page
    this form will have the following fields: username and password at the moment
    """
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name')