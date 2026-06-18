from django.urls import path 
from main.views import * 

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blogd/', views.blogd, name='blogd'),
    path('service/', views.service, name='service'),
    path('project/', views.project, name='project'),
    path('projectd/', views.projectd, name='projectd'),
    path('team/', views.team, name='team'),
    path('teamd/', views.teamd, name='teamd'),
    path('serviced/', views.serviced, name='serviced'),
    path('contacts/', views.contact, name='contact'),
    path('type/<slug:slug>/', views.mockup_type_detail, name='mockup_type_detail'),
    path('project/<slug:slug>/', views.project_detail, name='project_detail'),
]