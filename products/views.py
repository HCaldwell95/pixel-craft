from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductOption

# Show list of all products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

# Show details for one product
def product_detail(request, product_id):
    product = get_object_or_404(Product.objects.prefetch_related('options'), pk=product_id)
    return render(request, 'products/product_detail.html', {'product': product})

# Add item to cart
def add_to_cart(request):
    if request.method == "POST":
        option_id = request.POST.get('option')
        quantity = int(request.POST.get('quantity', 1))

        if not option_id:
            # Option wasn't selected — redirect back or show error
            return redirect('product_list')  # Or show message to select an option

        try:
            option = ProductOption.objects.get(id=option_id)
        except ProductOption.DoesNotExist:
            # Invalid option ID submitted
            return redirect('product_list')  # Or render an error

        product = option.product
        price = option.price
        cart = request.session.get('cart', [])
        item_exists = False

        for item in cart:
            if item['option_id'] == option.id:
                item['quantity'] += quantity
                item_exists = True
                break

        if not item_exists:
            cart.append({
                'product_id': product.id,
                'option_id': option.id,
                'quantity': quantity,
                'price': float(price),
            })
        request.session['cart'] = cart
        return redirect('cart')


# View cart contents
def cart(request):
    cart_items = []
    total_price = 0
    cart = request.session.get('cart', [])

    for item in cart:
        product = get_object_or_404(Product, id=item['product_id'])
        option = get_object_or_404(ProductOption, id=item['option_id'])

        item_price = float(item['price']) * item['quantity']
        total_price += item_price

        cart_items.append({
            'product': product,
            'option': option,
            'quantity': item['quantity'],
            'item_price': item_price,
        })

    return render(request, 'add_to_cart/add_to_cart.html', {
        'cart_items': cart_items, 
        'total_price': total_price
    })


# Remove item from cart
def remove_from_cart(request, option_id):
    cart = request.session.get('cart', [])
    cart = [item for item in cart if item['option_id'] != option_id]
    request.session['cart'] = cart
    return redirect('cart')
