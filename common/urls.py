# common/urls.py

from django.urls import path

from .views import *

urlpatterns = [

    path('',home,name='home'),
    path('search/',search,name='search'),
    path("contact/", contact, name="contact"),
    path("tip/",contact,name="tip"),
    path('project-types/', project_types, name='project_types'),
    path('project-type/<slug:slug>/', projects_by_type, name='projects_by_type'),
    path('clients/', companies, name='companies'),
    
    

]