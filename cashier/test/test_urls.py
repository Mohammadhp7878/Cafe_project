from django.test import SimpleTestCase
from django.urls import resolve, reverse
from cashier.views import DashboardView, ProductView, DeleteOrderView, ChangeStatusView

class TestUrls(SimpleTestCase):

    def test_dashboard(self):
        url = reverse('cashier:dashboard')
        self.assertEqual(resolve(url).func.view_class, DashboardView)

    def test_change(self):
        url = reverse('cashier:change-status')
        self.assertEqual(resolve(url).func.view_class, ChangeStatusView)

    def test_delete(self):
        url = reverse('cashier:delete_order', args=('order',))
        self.assertEqual(resolve(url).func.view_class, DeleteOrderView)