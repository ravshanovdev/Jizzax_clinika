from django.contrib import admin
from .models import Category, Product, ProductInventory, Discount, PaymentDetail, \
    OrderDetails, OrderItems, CartItem, Cart
from django.contrib import admin

admin.site.register(Category)
admin.site.register(ProductInventory)
admin.site.register(Discount)
admin.site.register(PaymentDetail)
admin.site.register(OrderItems)
admin.site.register(OrderDetails)
admin.site.register(CartItem)
admin.site.register(Cart)


class ProductList(admin.ModelAdmin):
    list_display = ['category', 'name', 'SKU', 'currency', 'price', 'created_at', 'inventory_id', 'discount_id']


admin.site.register(Product, ProductList)
