# projects/admin.py

from django.contrib import admin
from .models import *


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    prepopulated_fields = {
        'slug': ('title',)
    }

    inlines = [ProjectImageInline]

    list_display = (
        'title',
        'company',
        'project_type',
        'scale',
        'year',
        'views'
    )

    list_filter = (
        'project_type',
        'year'
    )

    search_fields = (
        'title',
        'company__name'
    )


admin.site.register(Company)
admin.site.register(ProjectType)
admin.site.register(Scale)