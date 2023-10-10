from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from accounts.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import UserAddress, UserPayment, ShoppingSession
from .serializers import UserAddressSerializer, UserPaymentSerializer, ShoppingSessionSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ExampleApiView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),
            'auth': str(request.auth)
        }
        return Response(content)


class RegistrationApiView(APIView):

    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]
        user = User(username=username)
        user.set_password(password)

        user.save()
        print(username)
        print(password)
        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "status": "success",
                "user_id": user.id,
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            }
        )


class UserAddressApiView(ListCreateAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer


class AddressUpdateDestroyAPiView(RetrieveUpdateDestroyAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer


class UserPaymentApiView(ListCreateAPIView):
    queryset = UserPayment.objects.all()
    serializer_class = UserPaymentSerializer


class ShoppingSessionApiView(ListCreateAPIView):
    queryset = ShoppingSession.objects.all()

    def get_serializer_class(self):
        return ShoppingSessionSerializer




