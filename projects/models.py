from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class Company(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='companies/')
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class ProjectType(models.Model):
    title = models.CharField(max_length=255)

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    main_image = models.ImageField(
        upload_to='project_types/'
    )

    short_description = models.TextField(
        blank=True,
        null=True
    )

    description = RichTextField()

    order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def get_absolute_url(self):

        return reverse(
            'projects_by_type',
            kwargs={'slug': self.slug}
        )

    @property
    def total_projects(self):

        return self.project_set.count()

    @property
    def total_views(self):

        return (
            self.project_set.aggregate(
                Sum('views')
            )['views__sum'] or 0
        )



class Scale(models.Model):
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.value


class Project(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    main_image = models.ImageField(upload_to='projects/main/')
    description = RichTextField()

    project_type = models.ForeignKey(
        ProjectType,
        on_delete=models.SET_NULL,
        null=True,
        related_name='projects'
    )

    scale = models.ForeignKey(
        Scale,
        on_delete=models.SET_NULL,
        null=True
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    year = models.PositiveIntegerField()
    is_featured = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='projects/gallery/')

    def __str__(self):
        return self.project.title