from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # Displays all products
    path('<int:product_id>/', views.product_detail, name='product_detail'),  # Displays individual product details
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('remove/<int:option_id>/', views.remove_from_cart, name='remove_from_cart'),
]
