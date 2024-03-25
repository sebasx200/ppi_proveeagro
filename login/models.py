from django import forms
from django.contrib.auth.models import User

# Create your models here.

class User(forms.Form):
    """
    this class is used to create a new user in the database with the following fields
    """
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']