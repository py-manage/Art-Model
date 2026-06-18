# company/models.py

from django.db import models
from ckeditor.fields import RichTextField


class About(models.Model):
    title = models.CharField(max_length=255)

    description = RichTextField()

    image = models.ImageField(upload_to='about/')

    experience = models.PositiveIntegerField(default=0)

    completed_projects = models.PositiveIntegerField(default=0)

    clients = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class About2(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()

    image_1 = models.ImageField(upload_to='about/')
    image_2 = models.ImageField(upload_to='about/')

    experience_years = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.title

class Client(models.Model):
    name = models.CharField(max_length=255)

    logo = models.ImageField(upload_to='clients/')

    website = models.URLField(blank=True)

    def __str__(self):
        return self.name

# reviews/models.py

from django.db import models
from projects.models import Project


class Review(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    name = models.CharField(max_length=255)

    email = models.EmailField()

    message = models.TextField()

    rating = models.PositiveIntegerField(default=5)

    created_at = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    

    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.full_name