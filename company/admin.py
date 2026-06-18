# reviews/admin.py

from django.contrib import admin
from .models import Review

# company/admin.py

from django.contrib import admin
from .models import *

admin.site.register(About)
admin.site.register(About2)

admin.site.register(Client)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'project',
        'rating',
        'is_active'
    )

    list_filter = (
        'rating',
        'is_active'
    )

    search_fields = (
        'name',
        'email'
    )