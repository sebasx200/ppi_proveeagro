from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SupplierForm, LocationForm
from .models import Supplier, Location, City, Department

# Create your views here.

@login_required
def suppliers_list(request):
    """
    this view is used to display the list of suppliers
    """

    suppliers = Supplier.objects.all()

    context = {
        'suppliers': suppliers
    }

    return render(request, 'supplier_crud/suppliers_list.html', context)

@login_required
def supplier_add(request):
    """
    this view is used to add a new supplier
    """
    if request.method == 'GET':
        
        departments = Department.objects.all()
        cities = City.objects.all()
        form_supplier = SupplierForm()
        location_form = LocationForm()
        context ={
            'departments': departments,
            'cities': cities,
            'form_supplier': form_supplier,
            'location_form': location_form
        }
        return render(request, 'supplier_crud/supplier_add.html', context)
    else:
        form = SupplierForm(request.POST)
        if form.is_valid():
            new_supplier = form.save(commit=False)
            new_supplier.created_by = request.user
            new_supplier.save()
            return redirect('suppliers_list')
        else:
            error = form.errors
            return render(request, 'supplier_crud/supplier_add.html', {'form': form, 'error': error})
        

