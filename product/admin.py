from django.contrib import admin
from .models import (Product,
                    ImageUpload,
                    Category,
                    # orderItem
                     ) 

admin.site.register(Product)
admin.site.register(ImageUpload)
admin.site.register(Category)
# admin.site.register(orderItem)
