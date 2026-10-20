from django.core.exceptions import ValidationError
from django.test import TestCase
from django.db import IntegrityError
from ..models import Product


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.product=Product(name="I phone",price=100, stock_count=10)

    def test_in_stock_property(self):
        self.assertTrue(self.product.stock_count)

        self.product.stock_count=0

        self.assertFalse(self.product.stock_count)

    def test_discount_price(self):
        self.assertEqual(self.product.discount_price(0),100)
        self.assertEqual(self.product.discount_price(50),50)

    def test_negative_price_validation(self):
        self.product.price=-100
        with self.assertRaises(ValidationError):
            self.product.clean()

    def test_negative_stock_count_validation(self):
            self.product.stock_count=-100
            with self.assertRaises(ValidationError):
                self.product.clean()
        
    def test_negative_price_constraint(self):
        product=Product(name="redmi",price=-100,stock_count=10)

        with self.assertRaises(IntegrityError):
            product.save()

    def test_negative_stock_count_constraint(self):
            product=Product(name="redmi",price=100,stock_count=-10)
    
            with self.assertRaises(IntegrityError):
                product.save()