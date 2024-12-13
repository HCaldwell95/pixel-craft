from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=100)
    cost = models.CharField(max_length=50)
    description = models.TextField()
    icon = models.ImageField(upload_to='services/icons/')

    def __str__(self):
        return self.title