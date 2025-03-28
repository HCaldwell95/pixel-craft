# accounts/forms.py
from django.contrib.auth.forms import UserChangeForm
from django import forms
from .models import UserProfile, CustomUser

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['favorite_category', 'phone']

class CustomUserChangeForm(UserChangeForm):
    # You can add custom fields here if needed
    class Meta:
        model = CustomUser  # or the default `User` model if you're not using `CustomUser`
        fields = ['username', 'email', 'first_name', 'last_name']
