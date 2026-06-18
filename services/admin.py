# services/admin.py

from django.contrib import admin
from .models import *


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    prepopulated_fields = {
        'slug': ('title',)
    }

    list_display = (
        'title',
        'views'
    )

admin.site.register(Service1)