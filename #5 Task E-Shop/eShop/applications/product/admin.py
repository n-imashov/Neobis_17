from django.contrib import admin

from .models import Product, ProductImage


class InlineProductImage(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ['image', ]


class ProductAdminDisplay(admin.ModelAdmin):
    inlines = [InlineProductImage, ]


admin.site.register(Product, ProductAdminDisplay)
