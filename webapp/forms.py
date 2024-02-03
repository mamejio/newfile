from django.forms import ModelForm, forms
from .models import Product, OrderItem

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class OrderForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'

