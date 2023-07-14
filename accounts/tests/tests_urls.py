from django.test import SimpleTestCase
from django.urls import resolve, reverse
from accounts.views import CashierLogin

class TestUrls(SimpleTestCase):

    def test_cashierlogin(self):
        url=reverse('accounts:cashierlogin')
        self.assertEqual(resolve(url).func.view_class, CashierLogin)


