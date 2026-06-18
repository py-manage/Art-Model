from django.db import models

# Create your models here.
from django.db import models
from django.utils.text import slugify

class MockupType(models.Model):
    """ Maket turlari (Masalan: Arxitekturaviy, Industrial, Interyer va hk.) """
    name = models.CharField(max_length=100, verbose_name="Maket turi nomi")
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True, verbose_name="Tavsif")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Maket turi"
        verbose_name_plural = "Maket turlari"


class Project(models.Model):
    """ Bajarilgan loyihalar (Portfolio) """
    title = models.CharField(max_length=250, verbose_name="Loyiha nomi")
    slug = models.SlugField(unique=True, blank=True)
    mockup_type = models.ForeignKey(MockupType, on_delete=models.CASCADE, related_name='projects', verbose_name="Maket turi")
    description = models.TextField(verbose_name="Loyiha haqida batafsil")
    main_image = models.ImageField(upload_to='projects/', verbose_name="Asosiy rasm")
    client_name = models.CharField(max_length=150, blank=True, verbose_name="Buyurtmachi/Mijoz nomi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Loyiha"
        verbose_name_plural = "Loyihalar"
        ordering = ['-created_at']


class Client(models.Model):
    """ Hamkorlar va Mijozlar logotiplari """
    name = models.CharField(max_length=100, verbose_name="Kompaniya nomi")
    logo = models.ImageField(upload_to='clients/', verbose_name="Logotip")
    website = models.URLField(blank=True, verbose_name="Veb-sayti (agar bo'lsa)")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mijoz/Hamkor"
        verbose_name_plural = "Mijoz va Hamkorlar"