# projects/urls.py

from django.urls import path

from .views import *

urlpatterns = [

    path('', projects,name='project'),
    path('<slug:slug>/',project_detail,name='project_detail'),
]