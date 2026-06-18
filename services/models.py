# services/models.py

from django.db import models
from ckeditor.fields import RichTextField


class Service(models.Model):
    title = models.CharField(max_length=255)

    slug = models.SlugField(unique=True)

    image = models.ImageField(upload_to='services/')

    short_description = models.TextField()

    description = RichTextField()

    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.text import slugify


class Service1(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    image = models.ImageField(upload_to='services/')
    icon = models.CharField(
        max_length=100,
        help_text="Masalan: flaticon-bed-1"
    )
 
    short_description = models.TextField()
    description = RichTextField()

    order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse(
            'service_detail',
            kwargs={'slug': self.slug}
        )


class ServicePageReview(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(
        max_length=50,
        blank=True
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name