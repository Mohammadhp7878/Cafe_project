from django.test import TestCase
from django.urls import reverse
from django.http import HttpRequest
from orders.models import Product, Order, Product_Order, Receipt
from orders.views import CartView, ReceiptView

# class CartViewTest(TestCase):
#     def test_get_cart_view(self):
#         response = self.client.get(reverse('cart_view'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'cart_page.html')

#     def test_post_cart_view(self):
#         response = self.client.post(reverse('cart_view'))
#         self.assertRedirects(response, reverse('cart.html'))
    

