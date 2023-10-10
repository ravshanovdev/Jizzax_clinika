from django.db import models

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProductInventory(models.Model):
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"mahsulot sonni: {self.quantity}ta "


class Discount(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    discount_percent = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


VALUE_TYPE = (
    ("uzs", "UZS"),
    ("euro", "EURO"),
    ("usd", "USD")
)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    name = models.CharField(max_length=255)
    photo1 = models.ImageField(upload_to='images/', blank=True)
    photo2 = models.ImageField(upload_to='images/', blank=True)
    photo3 = models.ImageField(upload_to='images/', blank=True)
    SKU = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    currency = models.CharField(max_length=10, choices=VALUE_TYPE, null=True)
    price = models.CharField(max_length=100000000000)
    created_at = models.DateTimeField(auto_now_add=True)
    inventory_id = models.ForeignKey(ProductInventory, on_delete=models.CASCADE, related_name='inventory')
    discount_id = models.ForeignKey(Discount, on_delete=models.CASCADE, related_name='discount', blank=True, null=True)

    def __str__(self):
        return self.name


VALUE_TYPE = (
    ('humo', 'HUMO'),
    ('uzcard', 'UzCard'),
    ('visa', 'VISA'),
    ('mastercard', 'MasterCard')
)


VALUE_TYPE_2 = (
    ('no paid', 'NO PAID'),
    ('paid', 'PAID')

)


class PaymentDetail(models.Model):
    amount = models.IntegerField()
    provider = models.CharField(max_length=255, choices=VALUE_TYPE)
    status = models.CharField(max_length=255, choices=VALUE_TYPE_2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status


class OrderDetails(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    payment_id = models.ForeignKey(PaymentDetail, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id.username


class OrderItems(models.Model):
    order_id = models.ForeignKey(OrderDetails, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"sotib oluvchi: {self.order_id}. Sotib olinayotgan mahsulot: {self.product_id.name}, miqdori {self.quantity} ta."


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField()
    total_price = models.FloatField(default=0)

    def __str__(self):
        return f"{self.user} - {self.total_price}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    price = models.FloatField(default=0)
    total_items = models.IntegerField(default=0)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_id} - {self.user}"


@receiver(pre_save, sender=CartItem)
def correct_price(sender, **kwargs):
    cart_items = kwargs['instance']
    price_of_product = Product.objects.get(id=cart_items.product_id.id)
    cart_items.price = cart_items.quantity * float(price_of_product.price)
    total_cart_items = CartItem.objects.filter(user=cart_items.user)
    cart_items.total_items = len(total_cart_items)

    cart = Cart.objects.get(id=cart_items.cart.id)
    cart.total_price = cart_items.price
    cart.save()


# @receiver(post_save, sender=CartItem)
# def correct_price(sender, instance, **kwargs):
#     price_of_product = instance.product_id
#     total_quantity = instance.quantity * float(price_of_product.price)
#     total_cart_items = CartItem.objects.filter(user=instance.user)
#     instance.total_items = len(total_cart_items)
#     instance.save()


