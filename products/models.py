from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db.models import Q
# Create your models here.



class CustomUser(AbstractUser):
    pass


class Product(models.Model):
    name=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    stock_count=models.IntegerField(default=0)

    class Meta:
        constraints=[
            models.CheckConstraint(
                condition=Q(price__gt=0),
                name='price_gt=0'

            ),
            models.CheckConstraint(
                condition=Q(stock_count__gte=0),
                name='stock_count_gte=0'
            )
        ]

    def discount_price(self, discount_percentage):
        return self.price * (1-discount_percentage/100)
    
    @property
    def in_stock(self):
        return self.stock_count > 0 
    
    def clean(self):
        if self.price < 0 :
            raise ValidationError('price must be positive')
        if self.stock_count < 0 :
            raise ValidationError('stock must be positive')

    

