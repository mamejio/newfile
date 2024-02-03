# models.py

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="No description available.")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class ProductTag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=255)
    comment = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.product} - {self.reviewer_name}"

class OrderItem(models.Model):
    customerName = models.CharField(max_length=255, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    price = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.customerName} - {self.product} - {self.quantity}"
