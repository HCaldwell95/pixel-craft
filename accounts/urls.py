from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

app_name='accounts'

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("register/", views.authView, name="register"),
    path("profile/", views.profile_view, name="profile"),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]
