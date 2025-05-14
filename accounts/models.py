from django.db import models, transaction
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

# Categories
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

# Profile Model
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    favorite_category = models.CharField(max_length=50, choices=DESIGN_CATEGORIES, blank=True, default='')
    phone = models.CharField(max_length=15, blank=True)
    picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

# Custom User Model
class CustomUser(AbstractUser):
    # Extend if needed in future
    pass

