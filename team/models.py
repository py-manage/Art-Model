from django.db import models

# Create your models here.
# team/models.py

class Team(models.Model):
    full_name = models.CharField(max_length=255)

    position = models.CharField(max_length=255)

    image = models.ImageField(upload_to='team/')

    bio = models.TextField(blank=True)

    instagram = models.URLField(blank=True)
    telegram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    def __str__(self):
        return self.full_name