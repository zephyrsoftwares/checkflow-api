"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful."""
        email = 'test@example.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized."""
        sample_data = [
            ['Test1@EXAMPLE.com', 'Test1@example.com', '0195670877'],
            ['test2@EXAMPLE.COM', 'test2@example.com', '0295670877'],
            ['TEST3@example.com', 'TEST3@example.com', '0395670877'],
            ['test4@example.COM', 'test4@example.com', '0495670877'],
        ]
        for data in sample_data:
            user = get_user_model().objects.create_user(
                email=data[0],
                password='test123',
                phone_number=data[2],
            )

            self.assertEqual(user.email, data[1])

    def test_new_user_without_email_raises_error(self):
        """Test creating user without email raises error."""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password='test123',
                phone_number='0195670877',
            )

    def test_create_new_superuser(self):
        """Test creating a new superuser."""
        user = get_user_model().objects.create_superuser(
            email="text@example.com",
            password='test123',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
