from product.models import Category, ImageUpload, OrderItem, Product, Order
from rest_framework.views import APIView  
from rest_framework.parsers import FormParser,  MultiPartParser
from .serializers import ( AddToCartSerializer, ImageUploadSerializer,
                             ListCartSerializer, OrderItemSerializer, OrderSerializer, ProductSerializer, CategorySerializer
                        )
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

# Create your views here.
class ImageUploadView(APIView):
    parsers = (FormParser,MultiPartParser)

    def post(self,request,*args,**kwargs):
        file_serializer = ImageUploadSerializer(data=request.data)
        if(file_serializer.is_valid()):
            file_serializer.save()
            return Response(file_serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(file_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class=CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class= CategorySerializer

class ImageUploadListView(generics.ListCreateAPIView):
    parsers = (FormParser,MultiPartParser)
    queryset = ImageUpload.objects.all()
    serializer_class=ImageUploadSerializer

class OrderItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class CartAddView(generics.CreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class=AddToCartSerializer

class CartListView(generics.ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class=ListCartSerializer

class CartUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class=ListCartSerializer

# class CartDeleteView(generics.DestroyAPIView):
#     queryset = OrderItem.objects.all()
#     serializer_class=DeleteCartSerializer

class OrderView(generics.ListCreateAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer