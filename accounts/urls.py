from django.urls import path, include
from . import views

urlpatterns = [
    path("signup/", views.authView, name="authView"),  # Assuming authView is defined in views.py
    path("accounts/", include("django.contrib.auth.urls")),  # Django auth URLs
    path('profile/edit/', views.edit_profile, name='edit_profile'),  # The edit_profile URL
]
