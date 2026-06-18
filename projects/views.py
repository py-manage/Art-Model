# projects/views.py

from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import *

from django.shortcuts import render,redirect
from django.core.paginator import Paginator

from .models import Project

from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q

from .models import *
from common.models import *

def projects(request):
    sliders = Slider.objects.filter(
                page__in=['projects', 'project'], 
                is_active=True
            ).order_by('order')
    projects = Project.objects.all().order_by('-created_at')

    project_type = request.GET.get('type')

    year = request.GET.get('year')

    scale = request.GET.get('scale')

    search = request.GET.get('q')

    # FILTER

    if project_type:
        projects = projects.filter(
            project_type__id=project_type
        )

    if year:
        projects = projects.filter(
            year=year
        )

    if scale:
        projects = projects.filter(
            scale__id=scale
        )

    if search:
        projects = projects.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search)
        )

    # PAGINATION

    paginator = Paginator(projects, 20)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    # STATS

    total_projects = Project.objects.count()

    total_this_year = Project.objects.filter(
        year=2026
    ).count()

    total_views = sum(
        Project.objects.values_list(
            'views',
            flat=True
        )
    )

    context = {
        'sliders': sliders,
        'page_obj': page_obj,
        'project_types': ProjectType.objects.all().order_by('order'),
        'types': ProjectType.objects.all(),
        
        'scales': Scale.objects.all(),

        'years': Project.objects.values_list(
            'year',
            flat=True
        ).distinct(),

        'total_projects': total_projects,

        'total_this_year': total_this_year,

        'total_views': total_views,

        # FILTERLARNI SAQLASH UCHUN

        'current_type': project_type,
        'current_year': year,
        'current_scale': scale,
        'current_search': search,
    }

    return render(
        request,
        'project.html',
        context
    )


from company.models import Review

def project_detail(request, slug):

    project = get_object_or_404(
        Project,
        slug=slug
    )

    project.views += 1
    project.save()
    sliders = Slider.objects.filter(is_active=True, page='project-details').order_by('order')
    
    if request.method == 'POST':

        Review.objects.create(

            project=project,

            name=request.POST.get('name'),

            email=request.POST.get('email'),

            message=request.POST.get('message')
        )

        return redirect(
            'project_detail',
            slug=project.slug
        )

    related_projects = Project.objects.exclude(
        id=project.id
    )[:4]

    context = {

        'project': project,
        'sliders': sliders,
        'related_projects': related_projects,
    }

    return render(
        request,
        'project-details.html',
        context
    )