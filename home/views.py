from django.shortcuts import render

# Create your views here.

def index(request):
    """
    Renders the home page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered home page template.
    """
    services = [
        {
            "title": "Logo Designs",
            "cost": "From £300",
            "description": "Create a unique logo that represents your brand identity.",
            "icon": "images/logo-design.png",
        },
        {
            "title": "Website Design",
            "cost": "From £480",
            "description": "Professional and responsive websites tailored to your needs.",
            "icon": "images/website-design.png",
        },
        {
            "title": "Stationary Design",
            "cost": "£150",
            "description": "Beautiful and professional stationary for your business.",
            "icon": "images/stationary-design.png",
        },
        {
            "title": "Business Cards",
            "cost": "£80",
            "description": "Custom-designed business cards that leave a lasting impression.",
            "icon": "images/business-card-design.png",
        },
        {
            "title": "Social Media Graphics",
            "cost": "From £120",
            "description": "Eye-catching graphics tailored for your social media platforms.",
            "icon": "images/social-media-design.png",
        },
        {
            "title": "Brochure Design",
            "cost": "From £200",
            "description": "High-quality brochures to showcase your products or services.",
            "icon": "images/brochure-design.png",
        },
        {
            "title": "Flyer Design",
            "cost": "£100",
            "description": "Creative flyer designs to effectively showcase your brand or event.",
            "icon": "images/flyer-design.png",
        },
        {
            "title": "Packaging Design",
            "cost": "From £250",
            "description": "Unique and functional packaging design for your products.",
            "icon": "images/packaging-design.png",
        },
        # Add more services here as needed
    ]
    return render(request, 'home/index.html', {"services": services})
