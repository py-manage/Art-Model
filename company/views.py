from django.shortcuts import render

# Create your views here.
# company/views.py

from django.shortcuts import render
from .models import About, Client,About2
from common.models import *

def about(request):


    about = About2.objects.first()
    sliders = Slider.objects.filter(is_active=True, page='about').order_by('order')

    clients = Client.objects.all()

    return render(
        request,
        'about.html',
        {
            'about': about,
            'clients': clients,
            'sliders': sliders,

        }
    )

# reviews/views.py

from django.shortcuts import redirect
from .models import Review
from projects.models import Project


def add_review(request, slug):

    project = Project.objects.get(slug=slug)

    if request.method == 'POST':

        Review.objects.create(
            project=project,
            full_name=request.POST.get('full_name'),
            email=request.POST.get('email'),
            message=request.POST.get('message'),
            rating=request.POST.get('rating'),
        )

    return redirect(
        'project_detail',
        slug=slug
    )




