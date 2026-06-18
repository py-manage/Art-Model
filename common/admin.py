from django.contrib import admin
from .models import *

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'page', 'order', 'is_active']
    list_filter = ['page', 'is_active']
    search_fields = ['title']
    ordering = ['page', 'order']

admin.site.register(Tel)
admin.site.register(Web)
admin.site.register(MobileSlider)
admin.site.register(HeroSection)
