from django.db import models
import uuid

class Product(models.Model):
    _id = models.CharField(max_length=24, unique=True)  # Unique ID from the JSON
    guid = models.UUIDField(default=uuid.uuid4, unique=True)  # GUID field for unique identifier
    about = models.TextField()  # Description about the product
    tags = models.JSONField(default=list, blank=True)  # Tags for filtering
    name = models.CharField(max_length=255, blank=True, null=True)  # Optional name for the product
    description = models.TextField(blank=True, null=True)  # Optional description
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Price as decimal
    image_url = models.URLField(max_length=500, blank=True, null=True)  # Image URL

    def __str__(self):
        return f"{self._id} - {self.guid}"
