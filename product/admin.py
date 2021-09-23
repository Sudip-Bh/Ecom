from django.contrib import admin
from .models import (Product,
                    ImageUpload,
                    Category,
                    Book
                    ) 

admin.site.register(Product)
admin.site.register(ImageUpload)
admin.site.register(Book)
admin.site.register(Category)
