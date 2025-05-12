from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from . import views

app_name='accounts'

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('profile/upload-picture/', views.upload_profile_picture, name='upload_profile_picture'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    
    path('accounts/', include('allauth.urls')),
    path('register/', views.authView, name='register'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    path('accounts/logout/', LogoutView.as_view(next_page='accounts:logged_out'), name='account_logout'),
    path('accounts/logged-out/', TemplateView.as_view(template_name='logged_out.html'), name='logged_out'),
]
