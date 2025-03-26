from django.urls import path
from . import views
from .views import authView

urlpatterns = [
    path("signup/", authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
]