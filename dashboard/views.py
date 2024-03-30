from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def suppliers_list(request):
    """
    this view is used to display the list of suppliers
    """
    return render(request, 'supplier_crud/suppliers_list.html', {})

@login_required
def supplier_add(request):
    """
    this view is used to add a new supplier
    """
    return render(request, 'supplier_crud/supplier_add.html', {})

