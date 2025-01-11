from django.contrib.auth.models import AbstractUser
from django.db import models

API_USER_TYPES = [
    ('consumer', 'Consumer'),
    ('supplier', 'Supplier'),

]
API_TRANSACTIONS_TYPES = [
    ('consume', 'Consume'),
    ('supply', 'Supply'),
]


class ApiUser(AbstractUser):
    CONSUMER = 'consumer'
    SUPPLIER = 'supplier'
    user_type = models.CharField(max_length=10,
                                 choices=API_USER_TYPES, default='consumer')
    ...


class Warehouse(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.id}:{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id}: {self.name}'


class Stock(models.Model):
    warehouse = models.ForeignKey(
        Warehouse, on_delete=models.CASCADE, related_name='stocks')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='stocks')
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('warehouse', 'product')

    def __str__(self):
        return f'{self.warehouse}: {self.product}  ({self.quantity})'


class Transaction(models.Model):
    CONSUME = 'consume'
    SUPPLY = 'supply'

    user = models.ForeignKey(
        ApiUser, on_delete=models.CASCADE, related_name='transactions')

    warehouse = models.ForeignKey(
        Warehouse, on_delete=models.CASCADE, related_name='transactions')

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='transactions')

    quantity = models.PositiveIntegerField()

    timestamp = models.DateTimeField(auto_now_add=True)

    transaction_type = models.CharField(
        max_length=10, choices=API_TRANSACTIONS_TYPES)

    def save(self, *args, **kwargs):
        if self.transaction_type == self.SUPPLY and self.user.user_type != ApiUser.SUPPLIER:
            raise ValueError("Only supplier can supply products.")
        if self.transaction_type == self.CONSUME and self.user.user_type != ApiUser.CONSUMER:
            raise ValueError("Only consumers can consume products.")

        stock, created = Stock.objects.get_or_create(
            warehouse=self.warehouse, product=self.product)
        if self.transaction_type == self.SUPPLY:
            stock.quantity += self.quantity
        elif self.transaction_type == self.CONSUME:
            if stock.quantity < self.quantity:
                raise ValueError("Not enough stock to consume.")
            stock.quantity -= self.quantity
        stock.save()
        super().save(*args, **kwargs)
