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
    initial_map = folium.Map(location=[6.2121913,-75.5771953], zoom_start=15)
    context = {'map': initial_map._repr_html_(), 'title': 'Medellin, Colombia'}

    return render(request, 'main.html', context)

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
                if user.is_authenticated:
                    return redirect('home')


def signup(request):
    """
    this function redirects to the signup.html file for sign up
    which is using the UserCreationForm from django
    """
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': CreateNewUser()})
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = CreateNewUser()
            return render(request, 'signup.html', {'form': form, 'error': 'The data you entered is not valid'})
                    
@login_required
def logout_sesion(request):
    """
    this function redirects to the main.html file when the user logs out
    """
    logout(request)
    return redirect('main')

@login_required
def home(request):
    """
    this function redirects to the home.html file for the home page when the user logs in or signs up
    """
    # the username is passed to the home.html file to be displayed
    username = request.user.username if request.user.is_authenticated else None
    
    return render(request, 'home.html', {'username': username})