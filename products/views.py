from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    products = Product.objects.all()  # You can apply filters here if needed
    return render(request, 'products/product_list.html', {'products': products})  # Correct template path

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/product_detail.html', {'product': product})  # Correct template path
