# blog/admin.py

from django.contrib import admin
from .models import *


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    prepopulated_fields = {
        'slug': ('title',)
    }

    list_display = (
        'title',
        'category',
        'views',
        'created_at'
    )

    search_fields = (
        'title',
    )


admin.site.register(BlogCategory)