from django.contrib import admin

# Register your models here.

# admin.py
from django.contrib import admin
from .models import Product, ProductOption

class ProductOptionInline(admin.TabularInline):
    model = ProductOption
    extra = 1  # Number of empty option fields displayed by default

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductOptionInline]
