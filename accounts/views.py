from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

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

# View for user registration (signup)
def authView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))  # Redirect to login after successful signup
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})
