from django.test import TestCase, Client
from django.urls import reverse
from .models import Product, Category

class ProductViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.products_url = reverse('product:new_product')
        self.category1 = Category.objects.create(
            name='Category 1',
            slug='category-1'
        )
        self.product1 = Product.objects.create(
            name='Product 1',
            category=self.category1,
        )
        self.category_slug_url = reverse('product:new_product', args=['category-1'])

    def test_product_view_GET(self):
        response = self.client.get(self.products_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/new_product.html')
        self.assertContains(response, 'Product 1')

    def test_product_view_GET_with_category_slug(self):
        response = self.client.get(self.category_slug_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/new_product.html')
        self.assertContains(response, 'Product 1')


class SetCookiTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.category1 = Category.objects.create(
            name='Category 1',
            slug='category-1'
        )
        self.product1 = Product.objects.create(
            name='Product 1',
            category=self.category1,
        )
        self.set_cookie_url = reverse('product:set_cookie', args=[self.product1.id])

    def test_set_cooki_GET(self):
        response = self.client.get(self.set_cookie_url)

        self.assertEqual(response.status_code, 302)
        self.assertIn('cart', response.cookies)
        self.assertEqual(response.cookies['cart'].value, str(self.product1.id))