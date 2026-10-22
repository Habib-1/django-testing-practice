from django.test import TestCase,SimpleTestCase
from ..models import Product
from django.urls import reverse

class TestHomePage(SimpleTestCase):
    #it's check only status code and ensure template is rendered or not
    # def test_homepage_status_code(self):
    #     response=self.client.get('/')
    #     self.assertEqual(response.status_code,200)
    def test_homepage_template(self):
        response=self.client.get('/')
        self.assertTemplateUsed(response,'index.html')
    #assertContains can check perticula renderable content and also check status 
    def test_homepage_content(self):
        response=self.client.get('/')
        self.assertContains(response,'Welcome to My Website',status_code=200)


class TestProductPage(TestCase):
    def setUp(self):
        Product.objects.create(name="laptop",price=100, stock_count=10)
        Product.objects.create(name="mobile",price=80, stock_count=8)

    def test_product_template(self):
        response=self.client.get(reverse('products'))
        self.assertTemplateUsed(response,'products.html')

    def test_products_context(self):
        response=self.client.get(reverse('products'))
        self.assertEqual(len(response.context['products']),2)
        self.assertContains(response,'laptop')
        self.assertNotContains(response,'There is no products')

    def test_products_no_object(self):
        Product.objects.all().delete()
        response=self.client.get(reverse('products'))
        self.assertContains(response,'There is no products')
        self.assertEqual(len(response.context['products']),0)

