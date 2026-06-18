# services/urls.py

from django.urls import path

from .views import *

urlpatterns = [

    path('',services,name='service'),

    path('<slug:slug>/',service_detail,name='service_details'),
]