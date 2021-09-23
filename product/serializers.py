from django.db.models import fields
from rest_framework import serializers
from .models import ImageUpload, Product,Category,Book
# from .serializers import CategorySerializer

class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUpload
        fields = ('file',)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Product
        fields  = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(
        many=True,
     )
    # books=BooksSerialiszer(many=True,read_only=True)#book always should same as model name or related name       
    class Meta:
        model = Category
        fields = '__all__'

class BooksSerialiszer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = Book
        fields = "__all__"





