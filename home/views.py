from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    """
    Renders the home page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered home page template.
    """
    return render(request, 'home/index.html')