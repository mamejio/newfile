

# Register your models here.
# admin.py

from django.contrib import admin
from .models import Product
from .models import ProductTag
from .models import ProductReview
from .models import OrderItem

admin.site.register(Product)
admin.site.register(ProductTag)
admin.site.register(ProductReview)
admin.site.register(OrderItem)
