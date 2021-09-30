from django.db import models
from django.core.validators import FileExtensionValidator
from django.db.models.base import Model
from django.urls import reverse

class ImageUpload(models.Model):
    file = models.FileField(default=None,blank=False,null=False,validators=[FileExtensionValidator(allowed_extensions=['jpg','png'])])

class Category(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return '%d: %s' % (self.id, self.title)

class Product(models.Model):
    product_tag = models.CharField(max_length=10)
    name =  models.CharField(max_length=100)
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    stock = models.IntegerField()
    quantity = models.IntegerField()
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)
    image = models.JSONField(blank=True,null=True)
    discount = models.FloatField(null=True,blank=True)
    # slug = models.SlugField(null=True,blank=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f'{self.product_tag}{self.name}'

    # def get_absolute_url(self):
    #     return reverse("product:products", kwargs={"slug": self.slug})
    

class OrderItem(models.Model):
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product,related_name="orderitem",on_delete=models.CASCADE,unique=True)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
    
    def get_total_product_price(self):
        return self.quantity*self.product.price

    def get_total_discount_product_price(self):
        return self.quantity * self.product.discount
    
    def get_amount_saved(self):
        return self.get_total_product_price() - self.get_total_discount_product_price()
    
    def get_final_price(self):
        if self.product.discount:
            return self.get_total_discount_product_price()
        return self.get_total_discount_product_price()

address_choices=(('B',"Billing"),
                ("S","Shiping"),)

class Address(models.Model):
    street_address=models.CharField(max_length=100)
    house_no=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=100)
    address_type=models.CharField(choices=address_choices,max_length=1)

    def __str__(self):
        return self.street_address

    class Meta:
        verbose_name_plural="Addresses"

class Payement(models.Model):
    amount = models.FloatField()
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount}"

class Order(models.Model):
    ref_code = models.CharField(max_length=20,blank=True,null=True)
    orderitem=models.ManyToManyField(OrderItem)
    order_date=models.DateTimeField()
    ordered=models.BooleanField(default=False)
    shipping_address=models.ForeignKey(Address,related_name="shipping_address",on_delete=models.CASCADE)
    billing_address=models.ForeignKey(Address,related_name="billing_address",on_delete=models.CASCADE)
    payment = models.ForeignKey(Payement,on_delete=models.CASCADE)
    is_delivered=models.BooleanField(default=False)
    is_received=models.BooleanField(default=False)
    refund_requested=models.BooleanField(default=False)
    refund_granted=models.BooleanField(default=False)

    def __str__(self):
        return self.ref_code  
    
    def get_total(self):
        total=0
        for order_product in self.products.all():
            total+=order_product.get_final_price()
        return total

class Refund(models.Model):
    order  =  models.ForeignKey(Order,on_delete=models.CASCADE,related_name="order")
    reason=models.TextField()
    accepted=models.BooleanField(default=False)
    email=models.EmailField()

    def __str__(self) -> str:
        return f"{self.pk}"
