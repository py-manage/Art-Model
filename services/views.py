# services/views.py

from django.shortcuts import render, get_object_or_404,redirect

from .models import *
from common.models import *

def services(request):
    sliders = Slider.objects.filter(is_active=True, page='services').order_by('order')
    services = Service1.objects.all().order_by('order')[:3]
    if request.method == 'POST':

        ServicePageReview.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            message=request.POST.get('message')
        )

        return redirect('service')
    reviews = ServicePageReview.objects.all()
    context={
        'sliders': sliders,
        'services': services,
         'reviews': reviews,
    }
    return render(
        request,
        'service.html',
        context
    )


def service_detail(request, slug):
    sliders = Slider.objects.filter(is_active=True, page='services-details').order_by('order')

    service = get_object_or_404(
        Service1,
        slug=slug
    )

    services = Service1.objects.exclude(
        id=service.id
    ).order_by('order')

    return render(
        request,
        'service-details.html',
        {
            'service': service,
            'services': services,
        'sliders': sliders,

        }
    )