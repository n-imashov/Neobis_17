from django.db import models

from applications.category.models import Category


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    in_stock = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, null=True,
                                 on_delete=models.SET_NULL,
                                 related_name='product')

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='image')
    image = models.ImageField(upload_to='products_photo')

    def __str__(self):
        return self.product.title
