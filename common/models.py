from django.db import models

# Create your models here.
import os
from django.db import models
from django.utils.text import slugify


def maket_tur_rasm_manzili(instance, filename):
    """Rasmlarni 'maketlar/turlari/filename' ko'rinishida yuklash uchun"""
    ext = filename.split('.')[-1]
    # Fayl nomini slug asosida chiroyli qilib o'zgartiramiz
    filename = f"{instance.slug}.{ext}"
    return os.path.join('maketlar/turlari/', filename)


class MaketTuri(models.Model):
    """Maket turlari uchun model (Masalan: Архитектурные, Промышленные)"""
    
    # Maket turi nomi (klacc nomi: tip)
    nomi = models.CharField(
        max_length=255, 
        verbose_name="Макет turi nomi", 
        unique=True
    )
    
    # Tizimdagi url manzili uchun (Masalan: /tipy-maketov/arhitekturnye/)
    slug = models.SlugField(
        max_length=255, 
        unique=True, 
        blank=True, 
        verbose_name="Slug (URL manzil)"
    )
    
    # Maket turi uchun rasm (image)
    rasm = models.ImageField(
        upload_to=maket_tur_rasm_manzili, 
        verbose_name="Maket turi rasmi"
    )
    
    # Maket turi haqida qisqacha ma'lumot (malumot)
    malumot = models.TextField(
        verbose_name="Kichik tavsif / Ma'lumot", 
        blank=True, 
        null=True
    )
    
    # Loyihalar tartibini boshqarish uchun
    tartib = models.PositiveIntegerField(
        default=0, 
        verbose_name="Ko'rinish tartibi"
    )

    class Meta:
        verbose_name = "Maket turi"
        verbose_name_plural = "Maket turlari"
        ordering = ['tartib', 'id']

    def __str__(self):
        return self.nomi

    def save(self, *args, **kwargs):
        """O'zbekcha yoki ruscha nomlardan avtomatik inglizcha slug yaratish"""
        if not self.slug:
            # Ruscha harflarni o'zgartirish uchun yoki oddiy slugify
            self.slug = slugify(self.nomi)
        super().save(*args, **kwargs)


class Web(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='companies/')
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Tel(models.Model):
    tel=models.IntegerField()
    
from django.db import models
from django.utils.text import slugify

class HeroSection(models.Model):
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    subtitle = models.TextField(blank=True, verbose_name="Quyi matn")
    background_image = models.FileField(upload_to='hero/', verbose_name="Background rasmi")
    secondary_image = models.FileField(upload_to='hero/', blank=True, null=True, verbose_name="Ikkinchi rasm")
    
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Sections"

    def __str__(self):
        return self.title

class Slider(models.Model):
    """Umumiy Slayder modeli - barcha sahifalar uchun"""
    
    PAGE_CHOICES = (
        ('home', 'Bosh sahifa'),
        ('projects', 'Projects'),
        ('project-details', 'Project Details'),
        ('project_types', 'Tip Maketov'),
        ('project_typesb', 'Tip Maketov by type'),
        ('about', 'About'),
        ('clients', 'Clients'),
        ('team', 'Team'),
        ('contact', 'Contact'),
        ('blog', 'Blog'),
        ('blog-details', 'Blog Details'),
        ('services', 'Services'),
        ('services-details', 'Services Details'),
        ('mobile', 'Mobil versiya uchun'),   # Telefon uchun alohida
    )

    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    subtitle = models.CharField(max_length=500, blank=True, verbose_name="Quyi sarlavha")
    image = models.ImageField(upload_to='sliders/', verbose_name="Rasm")
    
    page = models.CharField(max_length=50, choices=PAGE_CHOICES, default='home', verbose_name="Qaysi sahifada chiqsin")
    
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    is_active = models.BooleanField(default=True, verbose_name="Faol")
    
    button_text = models.CharField(max_length=100, blank=True, default="Batafsil", verbose_name="Tugma matni")
    button_url = models.CharField(max_length=200, blank=True, verbose_name="Tugma linki")
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['page', 'order']
        verbose_name = "Slayder"
        verbose_name_plural = "Slayderlar"

    def __str__(self):
        return f"{self.title} ({self.get_page_display()})"

class MobileSlider(models.Model):
    """Faqat mobil versiya uchun slayder"""
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='sliders/mobile/')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    button_text = models.CharField(max_length=100, blank=True)
    button_url = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['order']
        verbose_name = "Mobil Slayder"
        verbose_name_plural = "Mobil Slayderlar"

    def __str__(self):
        return self.title