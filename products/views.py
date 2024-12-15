from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductOption

def product_list(request):
    products = Product.objects.all()  # You can apply filters here if needed
    return render(request, 'products/product_list.html', {'products': products})  # Correct template path

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/product_detail.html', {'product': product})  # Correct template path

def add_to_cart(request):
    if request.method == "POST":
        option_id = request.POST.get('option')
        option = get_object_or_404(ProductOption, id=option_id)
        # Add the selected option to the cart
        # For example:
        # cart.add(option=option)
        return redirect('cart')
