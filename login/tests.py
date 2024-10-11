from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegistrationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.valid_payload = {
            "username": "testuser",
            "password": "TestPassword123!",
            "password2": "TestPassword123!",
            "email": "testuser@example.com",
            "first_name": "Test",
            "last_name": "User",
        }

    def _post_register(self, payload):
        return self.client.post(reverse("register"), data=payload, format="json")

    def test_user_registration_success(self):
        """
        Test to verify that user registration works with valid data.
        """
        response = self._post_register(self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, "testuser")

    def test_user_registration_password_mismatch(self):
        """
        Test to verify that user registration fails when passwords do not match.
        """
        invalid_payload = self.valid_payload.copy()
        invalid_payload["password2"] = "WrongPassword123"
        response = self._post_register(invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("password", response.data)


class UserSessionManagementTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = self._create_test_user()
        self.token = self._get_token_for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token.access_token}")

    def _create_test_user(self):
        return User.objects.create_user(
            username="testuser",
            password="TestPassword123!",
            email="testuser@example.com",
            first_name="Test",
            last_name="User",
        )

    def _get_token_for_user(self, user):
        return RefreshToken.for_user(user)

    def _post_login(self, payload):
        return self.client.post(reverse("get_token"), data=payload, format="json")

    def _get_user_profile(self):
        return self.client.get(reverse("user_profile"))

    def test_user_login_success(self):
        """
        Test to verify that user login works with correct credentials.
        """
        response = self._post_login(
            {
                "username": "testuser",
                "password": "TestPassword123!",
            }
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_user_access_protected_view_with_token(self):
        """
        Test to verify that authorized users can access protected views.
        """
        response = self._get_user_profile()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], self.user.username)

    def test_user_access_protected_view_without_token(self):
        """
        Test to verify that unauthorized users cannot access protected views.
        """
        self.client.credentials()  # Remove token
        response = self._get_user_profile()
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_login_incorrect_password(self):
        """
        Test to verify that user login fails with incorrect password.
        """
        response = self._post_login(
            {
                "username": "testuser",
                "password": "WrongPassword123!",
            }
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn(
            "No active account found with the given credentials",
            response.data.get("detail", ""),
        )

    def test_user_login_incorrect_username(self):
        """
        Test to verify that user login fails with incorrect username.
        """
        response = self._post_login(
            {
                "username": "wronguser",
                "password": "TestPassword123!",
            }
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn(
            "No active account found with the given credentials",
            response.data.get("detail", ""),
        )

    def test_token_refresh(self):
        """
        Test to verify that token refresh endpoint works.
        """
        response = self.client.post(
            reverse("refresh_token"),
            data={"refresh": str(self.token)},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)


class UserProfileTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = self._create_test_user()
        self.token = self._get_token_for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token.access_token}")

    def _create_test_user(self):
        return User.objects.create_user(
            username="testuser",
            password="TestPassword123!",
            email="testuser@example.com",
            first_name="Test",
            last_name="User",
        )

    def _get_token_for_user(self, user):
        return RefreshToken.for_user(user)

    def _get_user_profile(self):
        return self.client.get(reverse("user_profile"))

    def _put_user_profile(self, data):
        return self.client.put(reverse("user_profile"), data=data, format="json")

    def test_user_profile_retrieve(self):
        """
        Test to verify that user profile data is retrieved correctly.
        """
        response = self._get_user_profile()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "testuser")
        self.assertEqual(response.data["email"], "testuser@example.com")

    def test_user_profile_update(self):
        """
        Test to verify that user profile is updated correctly.
        """
        update_data = {
            "username": "updateduser",
            "email": "updateduser@example.com",
            "first_name": "Updated",
            "last_name": "User",
        }
        response = self._put_user_profile(update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, update_data["username"])
        self.assertEqual(self.user.email, update_data["email"])

    def test_user_profile_update_invalid_email(self):
        """
        Test to verify that updating user profile fails with invalid email.
        """
        invalid_data = {
            "username": "updateduser",
            "email": "invalidemail",
            "first_name": "Updated",
            "last_name": "User",
        }
        response = self._put_user_profile(invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email", response.data)
