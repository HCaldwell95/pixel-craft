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

# UserProfile model
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    favorite_category = models.CharField(max_length=50, choices=DESIGN_CATEGORIES, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

# CustomUser model, extending the default User model
class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  # Adding related_name to avoid clashes
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_user_permissions',  # Adding related_name to avoid clashes
        blank=True
    )

# Signal to automatically create/update the UserProfile whenever a User is saved
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
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

