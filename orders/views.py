from django.shortcuts import render
from django.views.generic import ListView

class OrderListView(ListView):
    template_name = 'orders/order_list.html'

    def get_queryset(self):
        return []