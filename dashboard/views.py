from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    """
    this function redirects to the home.html file for the home page when the user logs in or signs up
    """
    # the username is passed to the home.html file to be displayed
    username = request.user.username if request.user.is_authenticated else None
    
    return render(request, 'home.html', {'username': username})