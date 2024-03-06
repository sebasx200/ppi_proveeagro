# this file is created to create forms for login app
from django import forms
from .models import User

class CreateNewUser(forms.ModelForm):
    # this class is created to create the form for the sign up page
    # this form will have the following fields:
    # username and password
    class Meta:
        model = User
        fields = '__all__'