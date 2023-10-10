from django.db import models
from django.contrib.auth.models import AbstractUser, User
# from online_shopp.models import Product, Discount, Category, ProductInventory


# Create your models here.


# class CustomUser(AbstractUser):
#     telephone = models.CharField(max_length=13)


class UserAddress(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line1 = models.CharField(max_length=150)
    address_line2 = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=6)
    country = models.CharField(max_length=150)
    mobile = models.CharField(max_length=150)

    def __str__(self):
        return self.user_id.username


VALUE_TYPE = (
    ('CASH', "cash"),
    ('CHECKS', 'checks'),
    ('DEBIT CARDS', 'debit cards'),
    ('CREDIT CARDS', 'credit cards'),
    ('MOBILE PAYMENTS', 'mobile payments'),
    ('ELECTRONIC BANK TRANSFERS', 'electronic bank transfers')
)


VALUE_TYPE2 = (
    ('humo', 'HUMO'),
    ('uzcard', 'UzCard'),
    ('visa', 'VISA'),
    ('mastercard', 'MasterCard')
)


class UserPayment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    choose_payment_type = models.CharField(max_length=150, choices=VALUE_TYPE)
    provider = models.CharField(max_length=150, choices=VALUE_TYPE2)
    account_no = models.IntegerField()
    expiry = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.user_id.username


class ShoppingSession(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user_id.username





