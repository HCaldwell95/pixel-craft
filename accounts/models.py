from django.shortcuts import render, redirect
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


# Define a list of design categories for users to select their favorite category
DESIGN_CATEGORIES = [
    ('logo_designs', 'Logo Designs'),
    ('website_design', 'Website Design'),
    ('stationary_design', 'Stationary Design'),
    ('business_cards', 'Business Cards'),
    ('social_media_graphics', 'Social Media Graphics'),
    ('flyer_design', 'Flyer Design'),
    ('packaging_design', 'Packaging Design'),
    ('custom_prints', 'Custom Prints'),
]

# UserProfile model: Stores additional information about the user, such as their favorite design category
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    favorite_category = models.CharField(max_length=50, choices=DESIGN_CATEGORIES, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)  # If you want to store the user's phone

    def __str__(self):
        return self.user.username

# CustomUser model: Extends the default User model by adding a 'phone' field
class CustomUser(AbstractUser):
    
    phone = models.CharField(max_length=15, blank=True, null=True)  # Add the 'phone' field
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_user_permissions',  # Adding a related_name to resolve clash
        blank=True
    )


# Signal handler function: Automatically creates or updates a UserProfile when a User is saved
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()

# Home page view function: Renders the home page template when a request is made
def home_details(request):
    """
    Renders the home page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered home page template.
    """
    return render(request, 'home.html')

# Set the custom user model to be used for authentication (instead of the default Django User model)
AUTH_USER_MODEL = 'accounts.CustomUser'