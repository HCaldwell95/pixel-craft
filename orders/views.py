import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views.generic import ListView

def checkout(request):

    return render(request, 'orders/checkout.html')

stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def create_payment_intent(request):
    if request.method == 'POST':
        try:
            intent = stripe.PaymentIntent.create(
                amount=1000,  # Amount in pence = £10
                currency='gbp',
            )
            return JsonResponse({'clientSecret': intent.client_secret})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)