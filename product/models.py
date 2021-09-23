from django.core import validators
from django.db import models
from django.core.validators import FileExtensionValidator

class ImageUpload(models.Model):
    file = models.FileField(default=None,blank=False,null=False,validators=[FileExtensionValidator(allowed_extensions=['jpg','png'])])

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    test= models.CharField(max_length=255)

    def __str__(self):
        # return '%d: %s' %(self.id,self.title)
        return '%d: %s %s' % (self.id, self.title,self.test)

class Book(models.Model):
    title =models.CharField(max_length=155)
    category = models.ForeignKey(Category,related_name="books",on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13)
    pages = models.IntegerField()
    price = models.PositiveIntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    image = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        # return self.image
        return self.title

class Product(models.Model):
    product_tag  =    models.CharField(max_length=10)
    name =  models.CharField(max_length=100)
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    stock = models.IntegerField()
    quantity = models.IntegerField()
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f'{self.product_tag}{self.name}'



