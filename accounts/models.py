from django.shortcuts import render, redirect
from django.db import models

# Create your models here.

def home_details(request):
    """
    Renders the home page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered home page template.
    """
    return render(request, 'home.html')