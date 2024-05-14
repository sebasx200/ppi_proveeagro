from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import CreateNewUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from suppliers.models import Supplier
# Create your views here.

def main(request):
    """
    this function redirects to the index.html file for the main page
    """
    suppliers = Supplier.objects.all()
    context = {
        'suppliers': suppliers
    }
    return render(request, 'main.html', context)

def get_suppliers(request):
    suppliers_list = Supplier.objects.all()
    suppliers = [{'id': supplier.id, 'name': supplier.name, 'latitude': supplier.location.latitude,
                    'longitude': supplier.location.longitude, 'address': supplier.location.address} for supplier in suppliers_list]
    return JsonResponse(suppliers, safe=False)

def login_page(request):
    """
    this function redirects to the login.html file for login and uses the AuthenticationForm from django
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # get the user from the form
            user = form.get_user()
            # log in the user
            login(request, user)
            return redirect('home')
        else:
            username = request.POST['username']
            password = request.POST['password']
            # check if the user exists
            if User.objects.filter(username=username).exists():
                error = 'The password you entered is incorrect'
            else:
                error = 'The username you entered does not exist'

            return render(request, 'login.html', {'form': form, 'error': error})
    else:
        return render(request, 'login.html', {'form': AuthenticationForm()})


def signup(request):
    """
    this function redirects to the signup.html file for sign up
    which is using the UserCreationForm from django
    """
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'signup.html', {'form': form})
    else:
        form = CreateNewUser()
    
    return render(request, 'signup.html', {'form': form})

                    
@login_required
def logout_sesion(request):
    """
    this function redirects to the main.html file when the user logs out
    """
    logout(request)
    return redirect('main')