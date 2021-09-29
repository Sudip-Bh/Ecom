from django.db.models import fields
from rest_framework import serializers
from .models import ImageUpload, Product,Category 
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

# class orderItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=orderItem
#         fields='__all__'







