from django.http import HttpResponse
from django.shortcuts import render
from .forms import CreateNewUser

# Create your views here.

# this function redirects to the index.html file for the main page
def home(request):
    menu_navbar = [
        {'url': 'home', 'title': 'Home'},
        {'url': 'login', 'title': 'Login'},
        {'url': 'signup', 'title': 'Sign Up'}
    ]
    return render(request, 'home.html', {'menu_navbar': menu_navbar})

# this function redirects to the login.html file for login
def login(request):
    return render(request, 'login.html')

# this function redirects to the signup.html file for sign up
def signup(request):
    data = { 'form': CreateNewUser() }
    return render(request, 'signup.html', data)