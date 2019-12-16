from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_sucessfull(self):
        """Test creating a user when email is sucessful"""
        email = 'test@londonappdev.com'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test the email for user is normalized."""
        email = 'test@RICHARDLONG.COM'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test creating user with no email rasies error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """ Test creating a new superuser and saving"""
        super_user = get_user_model().objects.create_superuser(
            'richard.long@gmail.com',
            'test123'
        )
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
