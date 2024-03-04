# this file is created to create forms for login app
from django import forms

class CreateNewUser(forms.Form):
    # this class is created to create the form for the sign up page
    # this form will have the following fields:
    # username, email, password, and confirm password
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", max_length=100, widget=forms.PasswordInput)