
from django.urls import path
from .views import *

urlpatterns = [
    path('', about, name='about'),
    path('add-review/<slug:slug>/',add_review,name='add_review'),
]