from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from suppliers.forms import SupplierForm, LocationForm
from suppliers.models import City, Department
from .models import Farm, Farm_Type
from .forms import FarmForm
import json

# Create your views here.

@login_required
def farm_list(request):
    """
    this view is used to list all the farms
    """
    # get the list of farms
    farms = Farm.objects.all()

    # pass the list of farms to the template
    context = {
        'farms': farms
    }
    return render(request, 'farm_list.html', context)

@login_required
def farm_detail(request, farm_id):
    """
    this view is used to view a farm
    """
    # get the farm
    farm = Farm.objects.get(id=farm_id)

    # pass the farm to the template
    context = {
        'farm': farm
    }
    return render(request, 'farm_detail.html', context)

@login_required
def farm_add(request):
    """
    this view is used to add a new farm
    """
    if request.method == 'GET':
        
        # get the list of farm types to pass them to the template
        farm_types_list = Farm_Type.objects.all()
        # get the list of departments to pass them to the template
        departments_list = Department.objects.all()
        cities_list = City.objects.all()

        # convert the list of departments and cities to json to pass them to the template
        departments = json.dumps([{'id': department.id, 'name': department.name} for department in departments_list])
        cities = json.dumps([{'id': city.id, 'name': city.name, 'department': city.department.id} for city in cities_list])

        # create the forms
        form_farm = FarmForm()
        form_location = LocationForm()

        # pass the forms and the list of departments to the template
        context ={
            'farm_types': farm_types_list,
            'department_list': departments_list,
            'departments': departments,
            'cities': cities,
            'form_farm': form_farm,
            'form_location': form_location
        }
        return render(request, 'farm_add.html', context)
