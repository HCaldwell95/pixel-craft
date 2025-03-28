from django.urls import path
from .views import OrderListView  # Ensure this view exists

urlpatterns = [
    path('', OrderListView.as_view(), name='order_list'),
]
