from django.shortcuts import render
from .serizalizers import CategorySerializer, BodySerializer
from .models import Category, Blog
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
# views for category


class CategoryAPiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # filter_backends = (DjangoFilterBackend, )
    # filter_fields = ['id--', 'name--']


class AddCategoryApiView(CreateAPIView):
    permission_classes = [IsAdminUser, ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# views for blog
class BodyApiView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BodySerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ['id', 'name', ]


class AddBlogPostAPiView(CreateAPIView):
    permission_classes = [IsAdminUser, ]
    queryset = Blog.objects.all()

    def get_serializer_class(self):
        return BodySerializer


class RegistrationApiView(APIView):

    def post(self, request):
        username = request.data["username"]

        password = request.data['password']
        user = User(username=username)

        user.set_password(password)

        user.save()
        print(username)
        print(password)


        refresh = RefreshToken.for_user(user)

        return Response(
            {
                'status': 'success',
                'user_id': user.id,
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
        )





