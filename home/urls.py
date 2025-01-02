from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('diversity/', views.diversity_policy, name='diversity_policy'),

]