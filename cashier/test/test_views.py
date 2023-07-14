from django.test import TestCase, Client
from django.urls import reverse,resolve


# class TestDashboardView(TestCase):
#     def setUp(self):
#         self.client = Client()
#
#     def test_dashboard_GET(self):
#         response = self.client.get(reverse('cashier:dashboard', follow=True))
#         print(response)
#         self.assertEqual(response.status_code, 302)
#         self.assertTemplateUsed(response, 'cashier/cashier.html')


# class TestDeleteOrderView(TestCase):
#     def setUp(self):
#         self.client = Client()
#
#     def test_order_GET(self):
#         order_id = 11
#         response = self.client.get(reverse('cashier:delete_order', args=(order_id,)))
#         print(response)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'cashier/inc/delete.html')

