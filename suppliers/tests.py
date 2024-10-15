from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Supplier
from locations.models import Location, City, Department

# Create your tests here.


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


class SupplierVisualizationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self._create_user_and_login()
        self._create_location_hierarchy()
        self._create_suppliers()

    def _create_user_and_login(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="TestPassword123!",
            email="testuser@example.com",
            first_name="Test",
            last_name="User",
        )
        self.superuser = User.objects.create_superuser(
            username="adminuser",
            password="AdminPassword123!",
            email="adminuser@example.com",
            first_name="Admin",
            last_name="User",
        )
        self.client.login(username="testuser", password="TestPassword123!")

    def _create_location_hierarchy(self):
        self.department = Department.objects.create(name="Test Department")
        self.city = City.objects.create(name="Test City", department=self.department)
        self.location = Location.objects.create(
            address="Test Address", latitude=10.0, longitude=20.0, city=self.city
        )

    def _create_suppliers(self):
        Supplier.objects.create(
            name="Admin Supplier", location=self.location, created_by=self.superuser
        )
        Supplier.objects.create(
            name="User Supplier", location=self.location, created_by=self.user
        )

    def test_supplier_visualization_success(self):
        """Test to verify that authenticated users can see their suppliers and those added by admins."""
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse("suppliers-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Assuming both suppliers are visible
        supplier_names = [supplier["name"] for supplier in response.data]
        self.assertIn("Admin Supplier", supplier_names)
        self.assertIn("User Supplier", supplier_names)

    # def test_supplier_visualization_failure(self):
    #     """Test to verify that the appropriate error message is shown when the supplier list cannot be retrieved."""
    #     self.client.force_authenticate(user=self.user)

    #     # Assuming your system raises a 404 if no suppliers are found, you should remove all suppliers
    #     Supplier.objects.all().delete()

    #     response = self.client.get(reverse("suppliers-list"))
    #     self.assertEqual(
    #         response.status_code, status.HTTP_404_NOT_FOUND
    #     )  # Assuming the error code if suppliers can't be found
    #     self.assertIn("detail", response.data)
    #     self.assertEqual(
    #         response.data["detail"], "No suppliers found."
    #     )  # Customize the expected message based on your actual implementation


class SupplierModificationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self._create_user_and_login()
        self._create_location_hierarchy()
        self._create_suppliers()

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

    def _create_suppliers(self):
        self.supplier = Supplier.objects.create(
            name="Test Supplier", location=self.location, created_by=self.user
        )

    def test_supplier_modification_success(self):
        """Test to verify that authenticated users can modify their suppliers."""
        self.client.force_authenticate(user=self.user)
        updated_payload = {
            "name": "Updated Test Supplier",
            "email": "updated@supplier.com",
            "phone": "987654321",
            "location": {
                "address": "Updated Test Address",
                "latitude": 15.0,
                "longitude": 25.0,
                "city": self.city.id,
            },
        }
        response = self.client.put(
            reverse("suppliers-detail", args=[self.supplier.id]),
            data=updated_payload,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.supplier.refresh_from_db()
        self.assertEqual(self.supplier.name, "Updated Test Supplier")
        self.assertEqual(self.supplier.email, "updated@supplier.com")
        self.assertEqual(self.supplier.phone, "987654321")
        self.assertEqual(self.supplier.location.address, "Updated Test Address")
        self.assertEqual(self.supplier.location.latitude, 15.0)
        self.assertEqual(self.supplier.location.longitude, 25.0)

    def test_supplier_modification_failure(self):
        """Test to verify that supplier modification fails with invalid data."""
        self.client.force_authenticate(user=self.user)
        invalid_payload = {
            "name": "",
            "email": "updated@supplier.com",
            "phone": "987654321",
            "location": {
                "address": "Updated Test Address",
                "latitude": 15.0,
                "longitude": 25.0,
                "city": self.city.id,
            },
        }
        response = self.client.put(
            reverse("suppliers-detail", args=[self.supplier.id]),
            data=invalid_payload,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("name", response.data)

    # def test_supplier_modification_admin(self):
    #     """Test to verify that users cannot modify suppliers added by an admin."""
    #     self.client.force_authenticate(user=self.user)
    #     admin = User.objects.create_superuser(
    #         username="adminuser",
    #         password="AdminPassword123!",
    #         email="adminuser@example.com",
    #         first_name="Admin",
    #         last_name="User",
    #     )
    #     admin_supplier = Supplier.objects.create(
    #         name="Admin Supplier", location=self.location, created_by=admin
    #     )
    #     updated_payload = {
    #         "name": "Unauthorized Update",
    #         "email": "unauthorized@supplier.com",
    #         "phone": "999999999",
    #         "location": {
    #             "address": "Unauthorized Address",
    #             "latitude": 15.0,
    #             "longitude": 25.0,
    #             "city": self.city.id,
    #         },
    #     }
    #     response = self.client.put(
    #         reverse("suppliers-detail", args=[admin_supplier.id]),
    #         data=updated_payload,
    #         format="json",
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    #     self.assertIn("detail", response.data)
    #     self.assertEqual(
    #         response.data["detail"],
    #         "You do not have permission to perform this action.",
    #     )


class SupplierDeletionTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self._create_user_and_login()
        self._create_location_hierarchy()
        self._create_suppliers()

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

    def _create_suppliers(self):
        self.supplier = Supplier.objects.create(
            name="Test Supplier", location=self.location, created_by=self.user
        )

    def test_supplier_deletion_success(self):
        """Test to verify that authenticated users can delete their suppliers."""
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(
            reverse("suppliers-detail", args=[self.supplier.id])
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Supplier.objects.count(), 0)

    # def test_supplier_deletion_failure_no_server(self):
    #     """Test to verify that supplier deletion fails when the server is down."""
    #     self.client.force_authenticate(user=self.user)
    #     # Simulate server down situation
    #     # Since we can't actually take the server down in a unit test, we'll simulate this by mocking
    #     with self.settings(DEBUG=False):
    #         response = self.client.delete(
    #             reverse("suppliers-detail", args=[self.supplier.id])
    #         )
    #     self.assertEqual(
    #         response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR
    #     )  # Adjust based on actual implementation
    #     self.assertIn("detail", response.data)
    #     self.assertEqual(
    #         response.data["detail"], "Service unavailable. Please try again later."
    #     )  # Customize message as needed

    # def test_supplier_deletion_failure_admin_supplier(self):
    #     """Test to verify that users cannot delete suppliers added by an admin."""
    #     self.client.force_authenticate(user=self.user)
    #     admin = User.objects.create_superuser(
    #         username="adminuser",
    #         password="AdminPassword123!",
    #         email="adminuser@example.com",
    #         first_name="Admin",
    #         last_name="User",
    #     )
    #     admin_supplier = Supplier.objects.create(
    #         name="Admin Supplier", location=self.location, created_by=admin
    #     )
    #     response = self.client.delete(
    #         reverse("suppliers-detail", args=[admin_supplier.id])
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    #     self.assertIn("detail", response.data)
    #     self.assertEqual(
    #         response.data["detail"],
    #         "You do not have permission to perform this action.",
    #     )
