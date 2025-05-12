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

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create UserProfile after user creation
            UserProfile.objects.create(user=user)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


# Profile view to display user details along with UserProfile
@login_required
def profile_view(request):
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'accounts/profile.html', {
        'user': request.user,
        'profile': profile
    })

# Upload Profile Picture
@login_required
def upload_profile_picture(request):
    if request.method == 'POST' and request.FILES.get('profile_picture'):
        profile, created = UserProfile.objects.get_or_create(user=request.user)  # Ensures profile exists
        profile.picture = request.FILES['profile_picture']
        profile.save()
    return redirect('profile')


# View for editing the user profile
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after successful save
    else:
        form = UserChangeForm(instance=request.user)

    return render(request, 'account/edit_profile.html', {'form': form})

def authView(request):
    # Your authentication logic here
    return render(request, 'accounts/register.html')

def login_view(request):
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