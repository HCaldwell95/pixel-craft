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
            "product_id": "4",
        },
        {
            "title": "Website Design",
            "cost": "From £480",
            "description": "Professional and responsive websites tailored to your needs.",
            "icon": "images/website-design.png",
            "product_id": "23",
        },
        {
            "title": "Stationary Design",
            "cost": "£150",
            "description": "Beautiful and professional stationary for your business.",
            "icon": "images/stationary-design.png",
            "product_id": "2",
        },
        {
            "title": "Business Cards",
            "cost": "£80",
            "description": "Custom-designed business cards that leave a lasting impression.",
            "icon": "images/business-card-design.png",
            "product_id": "5",
        },
        {
            "title": "Social Media Graphics",
            "cost": "From £120",
            "description": "Eye-catching graphics tailored for your social media platforms.",
            "icon": "images/social-media-design.png",
            "product_id": "8",
        },
        {
            "title": "Custom Prints",
            "cost": "From £100",
            "description": "High-quality custom prints to bring your designs to life.",
            "icon": "images/custom-prints.png",
            "product_id": "3",
        },
        {
            "title": "Flyer Design",
            "cost": "£100",
            "description": "Creative flyer designs to effectively showcase your brand or event.",
            "icon": "images/flyer-design.png",
            "product_id": "12",
        },
        {
            "title": "Packaging Design",
            "cost": "From £250",
            "description": "Unique and functional packaging design for your products.",
            "icon": "images/packaging-design.png",
            "product_id": "7",
        },
    ]

    # Portfolio images data
    portfolio_images = [
        {
            "img_url": "images/logo-portfolio.jpg",
            "title": "Logo Design",
            "description": "A stunning logo for a modern brand.",
            "url": "/portfolio/#logo-design-portfolio"
        },
        {
            "img_url": "images/website-portfolio.png",
            "title": "Website Design",
            "description": "A sleek, responsive website design.",
            "url": "/portfolio/#website-design-portfolio"
        },
        {
            "img_url": "images/business-card-portfolio.jpg",
            "title": "Business Cards",
            "description": "Professionally designed business cards.",
            "url": "/portfolio/#business-card-portfolio"
        },
        {
            "img_url": "images/flyer-portfolio.png",
            "title": "Flyer Design",
            "description": "Eye-catching flyers that grab attention.",
            "url": "/portfolio/#flyer-portfolio"
        },
        {
            "img_url": "images/social-media-portfolio.png",
            "title": "Social Media Graphics",
            "description": "Engaging visuals for your social platforms.",
            "url": "/portfolio/#social-media-portfolio"
        },
        {
            "img_url": "images/stationary-portfolio.jpg",
            "title": "Stationary Design",
            "description": "Elegant stationary to elevate your brand.",
            "url": "/portfolio/#stationary-portfolio"
        },
    ]


    return render(request, 'home/index.html', {
    "services": services,
    "portfolio_images": portfolio_images,
    })

def diversity_policy(request):
    return render(request, 'home/diversity.html')

def work_with_me(request):
    return render(request, 'home/work-with-me.html')

def experience(request):
    return render(request, 'home/experience.html')

def portfolio(request):
    return render(request, 'home/portfolio.html')

def faq(request):
    return render(request, 'home/faq.html')

def about(request):
    return render(request, 'home/about.html')

def enquire(request):
    return render(request, 'home/enquire.html')

def submit_enquiry(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        # Handle the submission, like saving to the database or sending an email.
        return HttpResponse("Thank you for your enquiry!")
    return HttpResponse("Invalid request", status=400)

def blog(request):
    return render(request, 'home/blog.html')

def profile(request):
    return render(request, 'account/profile.html')
