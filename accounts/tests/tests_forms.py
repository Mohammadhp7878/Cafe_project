from django.test import TestCase
from accounts.forms import LoginForm

class TestLoginForm(TestCase):

    def test_valid_login_form(self):
        form_data = {
        'username': 'testuser',
        'password': 'testpassword',
        }
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_missing_username(self):
        form_data = {
        'password': 'testpassword',
        }
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)

    def test_missing_password(self):
        form_data = {
        'username': 'testuser',
        }
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password', form.errors)