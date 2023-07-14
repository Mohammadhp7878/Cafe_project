from django.test import SimpleTestCase
from django.urls import resolve, reverse
from home.views import SearchProduct

class TestUrls(SimpleTestCase):

    def test_searchproduct(self):
        url=reverse('home:search_product')
        print(url)
        self.assertEqual(resolve(url).func.view_class, SearchProduct)


