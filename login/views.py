from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CreateNewUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import folium

# Create your views here.

def main(request):
    """
    this function redirects to the index.html file for the main page
    """
    return render(request, 'main.html')

def login_page(request):
    """
    this function redirects to the login.html file for login and uses the AuthenticationForm from django
    """
    if request.method == 'GET':
        return render(request, 'login.html', {'form': AuthenticationForm()})
    else: 
        if request.method == 'POST':
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user is None:
                return render(request, 'login.html', 
                              {'form': AuthenticationForm(), 'error': AuthenticationForm.error_messages['invalid_login']})
            else:
                login(request, user)
                return redirect('home')


def signup(request):
    """
    this function redirects to the signup.html file for sign up
    which is using the UserCreationForm from django
    """
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': CreateNewUser()})
    else:
        if request.method == 'POST':
            form = CreateNewUser(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                if user is None:
                    return render(request, 'login.html', 
                              {'form': CreateNewUser(), 'error': CreateNewUser.error_messages['invalid_signup']})
                else:
                    login(request, user)
                    return redirect('home')
                    

def logout_sesion(request):
    """
    this function redirects to the main.html file when the user logs out
    """
    logout(request)
    return render(request, 'main.html')

@login_required
def home(request):
    """
    this function redirects to the home.html file for the home page when the user logs in or signs up
    """
    return render(request, 'home.html')