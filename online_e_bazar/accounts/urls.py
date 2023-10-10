from django.urls import path, include
from .views import ExampleApiView, RegistrationApiView, UserAddressApiView, \
    UserPaymentApiView, ShoppingSessionApiView, AddressUpdateDestroyAPiView
from rest_framework.authtoken import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('registration/', RegistrationApiView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api-token/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls')),
    path('address/', UserAddressApiView.as_view()),
    path('user_payment/', UserPaymentApiView.as_view()),
    path('shopping_session/', ShoppingSessionApiView.as_view()),
    path('WhoIm/', ExampleApiView.as_view()),
    path('address_edit_or_remove/<int:pk>/', AddressUpdateDestroyAPiView.as_view()),



]
