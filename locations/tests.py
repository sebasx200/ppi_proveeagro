from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from suppliers.models import Supplier
from locations.models import Location, City, Department


class SupplierRegistrationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self._create_user_and_login()
        self._create_location_hierarchy()
        self.valid_payload = self._build_valid_payload()

    def _create_user_and_login(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="TestPassword123!",
            email="testuser@example.com",
            first_name="Test",
            last_name="User",
        )
        self.client.login(username="testuser", password="TestPassword123!")

    def _create_location_hierarchy(self):
        self.department = Department.objects.create(name="Test Department")
        self.city = City.objects.create(name="Test City", department=self.department)
        self.location = Location.objects.create(
            address="Test Address", latitude=10.0, longitude=20.0, city=self.city
        )

    def _build_valid_payload(self):
        return {
            "name": "Test Supplier",
            "email": "test@supplier.com",
            "phone": "123456789",
            "location": {
                "address": "Test Address",
                "latitude": 10.0,
                "longitude": 20.0,
                "city": self.city.id,
            },
        }

    def test_supplier_registration_success(self):
        """
        Test to verify that authenticated users can successfully register a new supplier.
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            reverse("suppliers-list"), data=self.valid_payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Supplier.objects.count(), 1)
        self.assertEqual(Supplier.objects.get().name, "Test Supplier")

    def test_supplier_registration_invalid_data(self):
        """
        Test to verify that supplier registration fails with invalid data.
        """
        self.client.force_authenticate(user=self.user)
        invalid_payload = self._build_invalid_payload()
        response = self.client.post(
            reverse("suppliers-list"), data=invalid_payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def _build_invalid_payload(self):
        return {
            "name": "",
            "email": "test@supplier.com",
            "phone": "123456789",
            "location": {
                "address": "Test Address",
                "latitude": 10.0,
                "longitude": 20.0,
                "city": self.city.id,
            },
        }
