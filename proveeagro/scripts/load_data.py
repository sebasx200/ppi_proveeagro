"""
This script loads the data from the suppliers_medellin.xlsx file into the database.
"""

import os
import sys
import pandas as pd
import django

# Add the current directory to the Python path
sys.path.append(os.getcwd())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proveeagro.settings')
django.setup()

from dashboard.models import Supplier, Location

# Load the data from the excel file
df = pd.read_excel('proveeagro/data/suppliers_medellin.xlsx')

# split the coordinates into latitude and longitude
df[['latitude', 'longitude']] = df['coordinates'].str.split(',', expand=True)
# Create the locations and suppliers

# this loop iterates over the rows of the dataframe and creates a new location and supplier for each row
for index, row in df.iterrows():

    location = Location(address=row['address'], latitude=row['latitude'], longitude=row['longitude'], city_id=1)
    location.save()
    supplier = Supplier(name=row['name'], email=row['email'], phone=row['phone'], created_by_id=1, location_id=location.id)
    supplier.save()
    print(f'Supplier {supplier.name} created successfully')
