from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import ImageUpload, Order, OrderItem, Product,Category
# from .serializers import CategorySerializer

class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUpload
        fields = ('file',)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Product
        fields  = '__all__'

class CategoryShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):       
    class Meta:
        model = Category
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    # item_price = serializers.IntegerField(source="get_total_item_price")
    
    class Meta:
        model = OrderItem
        fields = ('product','quantity',)
class OrderItemSerializer(serializers.ModelSerializer):
    # item_price = serializers.IntegerField(source="get_total_item_price")
    
    class Meta:
        model = OrderItem
        fields = ('quantity',)



class AddToCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields=('quantity','product',)

class ListCartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = OrderItem
        fields='__all__'

class DeleteCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields='__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'  





