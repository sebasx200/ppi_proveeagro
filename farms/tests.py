from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from farms.models import Farm
from locations.models import Location, City, Department

# Create your tests here.


class FarmRegistrationTestCase(TestCase):
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
            "name": "Test Farm",
            "location": {
                "address": "Test Address",
                "latitude": 10.0,
                "longitude": 20.0,
                "city": self.city.id,
            },
        }

    def _build_invalid_payload(self):
        return {
            "name": "",
            "location": {
                "address": "",
                "latitude": 10.0,
                "longitude": 20.0,
                "city": self.city.id,
            },
        }

    def test_farm_registration_success(self):
        """
        Test to verify that authenticated users can successfully register a new farm.
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            reverse("farms-list"), data=self.valid_payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Farm.objects.count(), 1)
        self.assertEqual(Farm.objects.get().name, "Test Farm")

    def test_farm_registration_invalid_data(self):
        """
        Test to verify that farm registration fails with invalid data.
        """
        self.client.force_authenticate(user=self.user)
        invalid_payload = self._build_invalid_payload()
        response = self.client.post(
            reverse("farms-list"), data=invalid_payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class FarmVisualizationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self._create_user_and_login()
        self._create_location_hierarchy()
        self._create_farms()

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

    def _create_farms(self):
        Farm.objects.create(name="Farm 1", location=self.location, created_by=self.user)
        Farm.objects.create(name="Farm 2", location=self.location, created_by=self.user)

    def test_farm_visualization_success(self):
        """Test to verify that authenticated users can see their farms"""
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse("farms-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        farms_names = [farm["name"] for farm in response.data]
        self.assertIn("Farm 1", farms_names)
        self.assertIn("Farm 2", farms_names)


class FarmModificationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self._create_user_and_login()
        self._create_location_hierarchy()
        self._create_farms()

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

    def _create_farms(self):
        self.farm = Farm.objects.create(
            name="Test Farm", location=self.location, created_by=self.user
        )

    def test_farm_modification_success(self):
        """Test to verify that authenticated users can modify their farms."""
        self.client.force_authenticate(user=self.user)
        updated_payload = {
            "name": "Updated Test Farm",
            "location": {
                "address": "Updated Test Address",
                "latitude": 15.0,
                "longitude": 25.0,
                "city": self.city.id,
            },
        }
        response = self.client.put(
            reverse("farms-detail", args=[self.farm.id]),
            data=updated_payload,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.farm.refresh_from_db()
        self.assertEqual(self.farm.name, "Updated Test Farm")
        self.assertEqual(self.farm.location.address, "Updated Test Address")
        self.assertEqual(self.farm.location.latitude, 15.0)
        self.assertEqual(self.farm.location.longitude, 25.0)

    def test_farm_modification_failure(self):
        """Test to verify that farm modification fails with invalid data."""
        self.client.force_authenticate(user=self.user)
        invalid_payload = {
            "name": "",
            "location": {
                "address": "Updated Test Address",
                "latitude": 15.0,
                "longitude": 25.0,
                "city": self.city.id,
            },
        }
        response = self.client.put(
            reverse("farms-detail", args=[self.farm.id]),
            data=invalid_payload,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("name", response.data)


class FarmDeletionTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self._create_user_and_login()
        self._create_location_hierarchy()
        self._create_farms()

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

    def _create_farms(self):
        self.farm = Farm.objects.create(
            name="Test Farm", location=self.location, created_by=self.user
        )

    def test_farm_deletion_success(self):
        """Test to verify that authenticated users can delete their farms."""
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(
            reverse("farms-detail", args=[self.farm.id])
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Farm.objects.count(), 0)
