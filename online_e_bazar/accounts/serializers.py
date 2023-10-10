from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserAddress, UserPayment, ShoppingSession


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', ]


class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ['id', 'user_id', 'address_line1', 'address_line2', 'city', 'postal_code', 'country', 'mobile']


class UserPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPayment
        fields = ['user_id', 'choose_payment_type', 'provider', 'account_no', 'expiry']


class ShoppingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingSession
        fields = ['user_id', 'total', 'created_at']
