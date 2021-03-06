from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email = 'test@gmail.com', password = 'testpwd'):
    """Create a sample user"""

    return get_user_model().objects.create_user(email,password)

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        # test creating new user
        email = 'test@gmail.com'
        password = 'testpwd'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalise(self):
        """email in lower case"""
        email = "test@GMAIL.COM"
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())


    def test_new_user_invalid_email(self):
        """Email validation test"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Test123')


    def test_create_new_superuser(self):
        """Create superuser"""
        user = get_user_model().objects.create_superuser(
            'admin@gmail.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""

        tag = models.Tag.objects.create(
            user= sample_user(),
            name = 'Vegan'
        )
        self.assertEqual(str(tag), tag.name)
