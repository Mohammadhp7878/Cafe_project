from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from accounts.views import CashierLogin
from accounts.forms import LoginForm


class CashierLoginTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('accounts:cashierlogin')
        self.user = User.objects.create_user(
        username='testuser',
        password='testpassword'
        )


    def test_get_login_form(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertIsInstance(response.context['form'], LoginForm)


    def test_valid_login(self):
        response = self.client.post(self.login_url, {'username': '09199876543', 'password': 'Abb@s123'})
        self.assertRedirects(response, reverse('dashboard'))
    
    def test_invalid_login(self):
        response = self.client.post(self.login_url, {'username': '09199876543', 'password': 'Abb@s123'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertIsInstance(response.context['form'], LoginForm)
        self.assertContains(response, 'invalid username or password')

