from django.test import TestCase
from models import Order, Product_Order, Receipt, table
from products.models import Product

class OrderModelTest(TestCase):
    def test_str_representation(self):
        order = Order.objects.create()
        self.assertEqual(str(order), str(order.id))

    def test_default_status(self):
        order = Order.objects.create()
        self.assertEqual(order.status, Order.OrderStatus.Pending)

    def test_order_products_relationship(self):
        product1 = Product.objects.create(name='Product 1')
        product2 = Product.objects.create(name='Product 2')

        order = Order.objects.create()
        Product_Order.objects.create(order=order, product=product1, number=2, price=10.0)
        Product_Order.objects.create(order=order, product=product2, number=3, price=15.0)

        self.assertEqual(order.products.count(), 2)
        self.assertIn(product1, order.products.all())
        self.assertIn(product2, order.products.all())

class Product_OrderModelTest(TestCase):
    def test_number_field(self):
        product = Product.objects.create(name='Test Product')
        order = Order.objects.create()
        product_order = Product_Order.objects.create(order=order, product=product, number=5, price=10.0)

        self.assertEqual(product_order.number, 5)

    def test_price_field(self):
        product = Product.objects.create(name='Test Product')
        order = Order.objects.create()
        product_order = Product_Order.objects.create(order=order, product=product, number=5, price=10.0)

        self.assertEqual(product_order.price, 10.0)

class ReceiptModelTest(TestCase):
    def test_total_price_field(self):
        order = Order.objects.create()
        receipt = Receipt.objects.create(orders=order, total_price=100.0, final_price=100.0)

        self.assertEqual(receipt.total_price, 100.0)

    def test_final_price_field(self):
        order = Order.objects.create()
        receipt = Receipt.objects.create(orders=order, total_price=100.0, final_price=100.0)

        self.assertEqual(receipt.final_price, 100.0)

class tableModelTest(TestCase):
    def test_table_number_field(self):
        table_obj = table.objects.create(table_number=5, cafe_space_position='Some position')
        self.assertEqual(table_obj.table_number, 5)

    def test_cafe_space_position_field(self):
        table_obj = table.objects.create(table_number=5, cafe_space_position='Some position')
        self.assertEqual(table_obj.cafe_space_position, 'Some position')

