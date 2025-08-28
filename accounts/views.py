from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from .forms import RegisterForm
from .models import UserProfile

def authView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Optionally create a UserProfile
            UserProfile.objects.create(user=user)
            messages.success(request, 'Your account has been created successfully!')
            return redirect('accounts:login')  # Redirect to login after successful sign-up
        else:
            messages.error(request, 'There was an error with your form submission. Please check the details.')
    else:
        form = RegisterForm()

    return render(request, 'accounts/signup.html', {'form': form})


# Profile view to display user details along with UserProfile
@login_required
def profile_view(request):
    """
    Displays the user's profile along with the user profile data.
    """
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'accounts/profile.html', {
        'user': request.user, 
        'profile': profile})


# Upload Profile Picture
@login_required
def upload_profile_picture(request):
    """
    Allows users to upload and update their profile picture.
    """
    if request.method == 'POST' and request.FILES.get('profile_picture'):
        # Ensure the user has a profile
        profile, created = UserProfile.objects.get_or_create(user=request.user)

        # Assign the uploaded file to the correct field and handle errors
        try:
            profile.profile_picture = request.FILES['profile_picture']  # Use correct field name
            profile.save()
            messages.success(request, 'Your profile picture has been updated.')
        except Exception as e:
            messages.error(request, f"Failed to update profile picture: {e}")

    return redirect('profile')



# View for editing the user profile
@login_required
def edit_profile(request):
    """
    Allows users to edit their account details like username, email, etc.
    """
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after successful save
    else:
        form = UserChangeForm(instance=request.user)

    return render(request, 'accounts/edit_profile.html', {'form': form})


def login_view(request):
    """
    Handles user login and redirects to the homepage if successful.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Authenticate the user with the form's cleaned data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "You have been logged in successfully.")  # Ensure this message triggers
                # Add a dummy message to check if message system is working
                messages.info(request, "This is a test message.")
                return redirect('home')
            else:
                # Add an error if authentication failed
                form.add_error(None, "Invalid username or password.")

    else:
        form = AuthenticationForm()  # Initialize form for GET request

    return render(request, 'account/login.html', {'form': form})