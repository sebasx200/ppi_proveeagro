from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SupplierForm
from .models import Supplier

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
        form = SupplierForm()
        return render(request, 'supplier_crud/supplier_add.html', {'form': form})
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
        

