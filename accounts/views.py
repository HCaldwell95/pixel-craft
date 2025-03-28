from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UserProfileForm, CustomUserChangeForm



@login_required
def profile(request):
    # You can add any additional context here, such as user-specific data
    return render(request, 'accounts/profile.html', {'user': request.user})



# View for editing the user profile
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserChangeForm(instance=request.user, data=request.POST)
        profile_form = UserProfileForm(instance=request.user.userprofile, data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')  # Redirect after successful update
    else:
        user_form = UserChangeForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)

    return render(request, 'accounts/edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Create the user
            login(request, user)  # Log the user in immediately after registration
            return redirect('accounts:profile')  # Redirect to the profile page after successful signup
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})
