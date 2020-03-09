from django.test import TestCase
from .models import Product

# Create your tests here.


class ProductTests(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Product model
    """

    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')

    """
    Here we'll define the tests that we'll run against our
    Product views
    """
    def test_get_index_product_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")
