from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductOption

def product_list(request):
    products = Product.objects.all()  # You can apply filters here if needed
    return render(request, 'products/product_list.html', {'products': products})  # Correct template path


def product_detail(request, product_id):
    product = get_object_or_404(Product.objects.prefetch_related('options'), pk=product_id)

    context = {
        'product': product
    }
    return render(request, 'products/product_detail.html', context)



def add_to_cart(request):
    if request.method == "POST":
        option_id = request.POST.get('option')
        option = get_object_or_404(ProductOption, id=option_id)
        quantity = int(request.POST.get('quantity', 1))  # Default quantity to 1 if not provided

        # Check if the cart already exists in the session
        cart = request.session.get('cart', [])

        # Check if the option already exists in the cart, and if so, update the quantity
        item_exists = False
        for item in cart:
            if item['option_id'] == option.id:
                item['quantity'] += quantity
                item_exists = True
                break

        if not item_exists:
            # Add the new item to the cart
            cart.append({
                'option_id': option.id,
                'quantity': quantity
            })

        # Save the cart back to the session
        request.session['cart'] = cart

        return redirect('cart')  # Redirect to the cart view
