from rest_framework.generics import ListAPIView, ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, \
    RetrieveUpdateAPIView

from online_shopp.models import Product, Category, ProductInventory, Discount, PaymentDetail, \
    OrderDetails, OrderItems, CartItem, Cart

from online_shopp.serializers import ProductSerializer, CategorySerializer, \
    ProductInventorySerializer, DiscountSerializer, \
    PaymentDetailSerializer, OrderDetailsSerializer, \
    OrderItemsSerializer, CartItemSerializer, CartSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class ProductApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['id', 'name', ]


class OrderItemsViewSet(viewsets.ModelViewSet):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer


# class ProductApiView(APIView):
#     def get(self, request):
#         category = self.request.query_params.get('category')
#         if category:
#             queryset = Product.objects.filter(category__name=category)
#         else:
#             queryset = Product.objects.all()
#
#         serializer_class = ProductSerializer(queryset, many=True)
#         return Response(serializer_class.data)


class ProductCreateApiView(CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated, )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_filters = ['id', 'name']


class DetailProductApiView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# buni hali Ustozdan surashim kerak kerak yoki kerak emasligi va hokazo. Modelga qarasang esinga keladi
class ProductInventoryApiView(ListAPIView):
    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer


# balki buni views da qilish kerak emasdur chunki qidorni ozi alohida yaratish kerak emasku
# class ProductInventoryApiView(viewsets.ModelViewSet):
#     queryset = ProductInventory.objects.all()
#     serializer_class = ProductInventorySerializer


# balki buni views da qilish kerak emasdur chunki qidorni ozi alohida yaratish kerak emasku
class DiscountApiView(ListCreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


class PaymentDetailApiView(ListCreateAPIView):
    queryset = PaymentDetail.objects.all()
    serializer_class = PaymentDetailSerializer


class PaymentUpdateRemoveApiView(RetrieveUpdateDestroyAPIView):
    queryset = PaymentDetail.objects.all()
    serializer_class = PaymentDetailSerializer


class OrderDetailsApiview(ListCreateAPIView):
    queryset = OrderDetails.objects.all()
    serializer_class = OrderDetailsSerializer


class OrderItemsApiView(ListCreateAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer


# class PaymentDetailApiView(viewsets.ModelViewSet):
#     queryset = PaymentDetail.objects.all()
#     serializer_class = PaymentDetailSerializer


# class CartItemApiView(viewsets.ModelViewSet):
#     queryset = CartItem.objects.all()
#     serializer_class = CartItemSerializer
#
#
# class CartApiView(viewsets.ModelViewSet):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer

# test uchun
class Demo(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'success': "you authenticated"})


class CartItemApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self):
        pass

    def update(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass
