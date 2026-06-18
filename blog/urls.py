# blog/urls.py

from django.urls import path

from .views import *

urlpatterns = [
    path('', blogs,name='blog'),
    path('<slug:slug>/',blog_detail,name='blog_detail'),
]