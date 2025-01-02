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
    # Services data
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
            "title": "Custom Prints",
            "cost": "From £100",
            "description": "High-quality custom prints to bring your designs to life.",
            "icon": "images/custom-prints.png"
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
    ]

    # Portfolio images data
    portfolio_images = [
        {
            "img_url": "images/logo-portfolio.jpg",
            "title": "Logo Design",
            "description": "A stunning logo for a modern brand."
        },
        {
            "img_url": "images/website-portfolio.png",
            "title": "Website Design",
            "description": "A sleek, responsive website design."
        },
        {
            "img_url": "images/business-card-portfolio.jpg",
            "title": "Business Cards",
            "description": "Professionally designed business cards."
        },
        {
        "img_url": "images/flyer-portfolio.png",
        "title": "Flyer Design",
        "description": "Eye-catching flyers that grab attention."
        },
        {
            "img_url": "images/social-media-portfolio.png",
            "title": "Social Media Graphics",
            "description": "Engaging visuals for your social platforms."
        },
        {
            "img_url": "images/stationary-portfolio.jpg",
            "title": "Stationary Design",
            "description": "Elegant stationary to elevate your brand."
        },
    ]

    return render(request, 'home/index.html', {
    "services": services,
    "portfolio_images": portfolio_images,
    })
