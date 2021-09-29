from django.core import validators
from django.db import models
from django.core.validators import FileExtensionValidator
from django.db.models.base import Model

class ImageUpload(models.Model):
    file = models.FileField(default=None,blank=False,null=False,validators=[FileExtensionValidator(allowed_extensions=['jpg','png'])])

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        # return '%d: %s' %(self.id,self.title)
        return self.title


product_choice=(
    ('np',"Not Published "),
    ('p',"Published"),
   )
 
class Product(models.Model):
    product_tag  = models.CharField(max_length=10)
    name =  models.CharField(max_length=100)
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()
    status = models.CharField(choices=product_choice,max_length=100)
    date_created = models.DateField(auto_now_add=True)
    discount=models.FloatField(blank=True,null=True)
    image = models.JSONField()

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f'{self.product_tag}{self.name}'

class orderItem(models.Model):
    ordered=models.BooleanField(default=False)
    product = models.ForeignKey(Product,related_name="orderItem",on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()

    def get_total_item_price(self):
        return self.quantity*self.product.price

    def __str__(self) -> str:
        return f'{self.quantity} of {self.product.item}'
