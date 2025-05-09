from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

app_name='accounts'

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('profile/upload-picture/', views.upload_profile_picture, name='upload_profile_picture'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    
    path('accounts/', include('allauth.urls')),
    path('register/', views.authView, name='register'),
]
