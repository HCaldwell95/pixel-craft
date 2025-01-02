from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('diversity/', views.diversity_policy, name='diversity_policy'),
    path('work-with-me/', views.work_with_me, name='work_with_me'),
    path('experience/', views.experience, name='experience'),
]