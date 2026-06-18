# blog/models.py

from django.db import models
from ckeditor.fields import RichTextField


class BlogCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name




from django.utils.text import slugify

class Blog(models.Model):

    title = models.CharField(max_length=255)

    slug = models.SlugField(unique=True, blank=True)

    image = models.ImageField(upload_to='blog/')

    category = models.ForeignKey(
        BlogCategory,
        on_delete=models.SET_NULL,
        null=True
    )

    content = RichTextField()

    views = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class BlogReview(models.Model):

    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    name = models.CharField(max_length=120)

    email = models.EmailField()

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name