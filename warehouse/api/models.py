from django.contrib.auth.models import AbstractUser
from django.db import models

API_USER_TYPES = [
    ('consumer', 'Consumer'),
    ('supplier', 'Supplier'),

]


class ApiUser(AbstractUser):
    user_type = models.CharField(max_length=10,
                                 choices=API_USER_TYPES, default='consumer')
    ...


class Warehouse(models.Model):
    name = models.CharField(max_length=128)


class Product(models.Model):
    name = models.CharField(max_length=255)
    warehouse = models.ForeignKey(
        Warehouse,  related_name='products', on_delete=models.CASCADE)
    supplier = models.ForeignKey(
        ApiUser, related_name='products', on_delete=models.SET_NULL, null=True)
    amount = models.PositiveIntegerField()
