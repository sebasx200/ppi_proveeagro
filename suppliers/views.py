from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SupplierForm, LocationForm
from .models import Supplier, Location, City, Department
from .serializer import SupplierSerializer, LocationSerializer, DepartmentSerializer, CitySerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
import json

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

    return render(request, 'suppliers_list.html', context)

@login_required
def supplier_add(request):
    """
    this view is used to add a new supplier
    """
    if request.method == 'GET':
        
        # get the list of departments to pass them to the template
        departments_list = Department.objects.all()
        cities_list = City.objects.all()
        # convert the list of departments and cities to json to pass them to the template
        departments = json.dumps([{'id': department.id, 'name': department.name} for department in departments_list])
        cities = json.dumps([{'id': city.id, 'name': city.name, 'department': city.department.id} for city in cities_list])
        # create the forms
        form_supplier = SupplierForm()
        location_form = LocationForm()
        # pass the forms and the list of departments to the template
        context ={
            'department_list': departments_list,
            'departments': departments,
            'cities': cities,
            'form_supplier': form_supplier,
            'location_form': location_form
        }
        return render(request, 'supplier_add.html', context)
    
    else:
        # if the request is POST, get the forms data
        location_form = LocationForm(request.POST)
        supplier_form = SupplierForm(request.POST)

        # check if the forms are valid
        if location_form.is_valid() and supplier_form.is_valid():

            # save the forms data
            new_location = location_form.save(commit=False)
            new_location.city_id = request.POST.get('city')
            new_location.save()
            new_supplier = supplier_form.save(commit=False)
            new_supplier.created_by = request.user
            new_supplier.location = new_location
            new_supplier.save()
        
            return redirect('suppliers_list')
        else:
            error = supplier_form.errors + location_form.errors
            context = {
                'form_supplier': supplier_form,
                'location_form': location_form,
                'error': error
            }   
            return render(request, 'supplier_add.html', context)
        
class SupplierView(viewsets.ModelViewSet):
    """
    this class is used to create the CRUD views for the suppliers
    """
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Supplier.objects.filter(created_by=self.request.user.id)

class LocationView(viewsets.ReadOnlyModelViewSet):
    """
    this class is used to get the list of locations
    """
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]
    queryset = Location.objects.all()

class CityView(viewsets.ReadOnlyModelViewSet):
    """
    this class is used to get the list of cities
    """
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticated]
    queryset = City.objects.all()

class DepartmentView(viewsets.ReadOnlyModelViewSet):
    """
    this class is used to get the list of departments
    """
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]
    queryset = Department.objects.all()