from django.test import SimpleTestCase
from django.urls import reverse, resolve
from orders.views import CartView, ReceiptView

class TestUrls(SimpleTestCase):
    def test_cart_url_resolves(self):
        url = reverse('cart_view')
        self.assertEqual(resolve(url).func.view_class, CartView)

    def test_receipt_url_resolves(self):
        url = reverse('receipt')
        self.assertEqual(resolve(url).func.view_class, ReceiptView)
