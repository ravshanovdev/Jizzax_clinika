from django.urls import path
from .views import DetailProductApiView, \
    ProductInventoryApiView, DiscountApiView, PaymentDetailApiView, \
    OrderDetailsApiview, OrderItemsApiView, \
    OrderItemsViewSet, CartItemApiView, ProductApiView,\
    ProductCreateApiView, CategoryApiView, Demo, PaymentUpdateRemoveApiView

urlpatterns = [
    path('', ProductApiView.as_view()),
    # path('demo/', Demo.as_view()),
    path('category/', CategoryApiView.as_view()),
    path('detail/<int:pk>/', DetailProductApiView.as_view()),
    path('inventory/', ProductInventoryApiView.as_view()),
    path('discounts/', DiscountApiView.as_view()),
    path('payments/', PaymentDetailApiView.as_view()),
    path('order_detail/', OrderDetailsApiview.as_view()),
    path('AddProduct/', ProductCreateApiView.as_view()),
    path('order_items/', OrderItemsApiView.as_view()),
    path('cart-item/', CartItemApiView.as_view()),
    path('payment_edit_or_remove/<int:pk>/', PaymentUpdateRemoveApiView.as_view()),






]


# urls.py
# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# # router.register(r'products', ProductViewSet, basename='product')
# router.register(r'order-items', OrderItemsViewSet, basename='order-items')
# # router.register(r'product-inventory', ProductInventoryApiView, basename='product-inventory')
# router.register(r'payment-detail', PaymentDetailApiView, basename='payment-detail')
# router.register(r'cart-item', CartItemApiView, basename='cart_item')
# router.register(r'cart', CartApiView, basename='cart')
#
# urlpatterns = router.urls
