from django.shortcuts import render

# Create your views here.
# common/views.py

from django.shortcuts import render

from projects.models import Project
from blog.models import Blog
from services.models import Service1,Service
from company.models import Client,Review,About2
from team.models import Team
from blog.models import *
from .models import *
def home(request):
    about = About2.objects.first()

    blogs = Blog.objects.order_by(
        '-created_at'
    )
    services = Service1.objects.all().order_by('order')[:3]

    hero = HeroSection.objects.filter(is_active=True).first()  # birinchi faol hero
    featured_projects = Project.objects.filter(
        is_featured=True
    )[:12]

    latest_blogs = Blog.objects.order_by(
        '-created_at'
    )[:3]


    companies = Company.objects.all().order_by('id')


    clients = Client.objects.all()

    team = Team.objects.all()[:4]

    context = {
        'featured_projects': featured_projects,
        'latest_blogs': latest_blogs,
        'services': services,
        'clients': clients,
        'team': team,
        'hero': hero,
        'about': about,
        'blogs': blogs,
        'companies': companies,

    }

    return render(
        request,
        'index.html',
        context
    )

# common/views.py
from django.shortcuts import render
from django.db.models import Q
from projects.models import Project
from blog.models import Blog  # Blog modelingiz bo'lsa


def search(request):
    query = request.GET.get('q', '').strip()
    
    projects = []
    blogs = []
    results_count = 0

    if query:
        # Loyihalarni qidirish
        projects = Project.objects.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query)
        ).order_by('-created_at')

        # Blog'larni qidirish
        blogs = Blog.objects.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query)
        ).order_by('-created_at')

        results_count = projects.count() + blogs.count()

    context = {
        'query': query,
        'projects': projects[:12],
        'blogs': blogs[:12],
        'results_count': results_count,
    }
    return render(request, 'search_results.html', context)
from django.db.models import Q

def searssch(request):

    query = request.GET.get('q')

    projects = Project.objects.filter(
        Q(title__icontains=query)
    )

    blogs = Blog.objects.filter(
        Q(title__icontains=query)
    )

    context = {
        'query': query,
        'projects': projects,
        'blogs': blogs,
    }

    return render(
        request,
        'search.html',
        context
    )

def contact(request):
    """ Kontaktlar sahifasi """
    sliders = Slider.objects.filter(is_active=True, page='contact').order_by('order')
    context={
        'sliders': sliders,
    }
    return render(request, 'contact.html',context)

from projects.models import *
from django.core.paginator import Paginator

from django.shortcuts import render


from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator



from django.db.models import Q
from django.shortcuts import render
from django.core.paginator import Paginator

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q, Sum


def project_types(request):
    projects = Project.objects.all().order_by('-created_at')
    sliders = Slider.objects.filter(is_active=True, page='project_types').order_by('order')
    # Filterlar
    selected_type = request.GET.get('type')
    year = request.GET.get('year')
    scale = request.GET.get('scale')
    search = request.GET.get('q')

    if selected_type:
        projects = projects.filter(project_type__id=selected_type)
    if year:
        projects = projects.filter(year=year)
    if scale:
        projects = projects.filter(scale__id=scale)
    if search:
        projects = projects.filter(
            Q(title__icontains=search) | Q(description__icontains=search)
        )

    paginator = Paginator(projects, 12)
    page_obj = paginator.get_page(request.GET.get('page'))

    # ================== STATISTIKA ==================
    total_projects = Project.objects.count()
    total_this_year = Project.objects.filter(year=2026).count()
    total_views = Project.objects.aggregate(Sum('views'))['views__sum'] or 0

    context = {
        'page_obj': page_obj,
        'project_types': ProjectType.objects.all().order_by('order'),
        
        'scales': Scale.objects.all(),
        'years': Project.objects.values_list('year', flat=True).distinct().order_by('-year'),

        'total_projects': total_projects,
        'total_this_year': total_this_year,
        'total_views': total_views,
        'sliders': sliders,
        'current_type': selected_type,
        'current_year': year,
        'current_scale': scale,
        'current_search': search,
    }

    return render(request, 'tip/project_types.html', context)

def projects_by_types(request, slug):

    """Bitta tur bo'yicha loyihalar"""
    project_type = get_object_or_404(ProjectType, slug=slug)
    
    projects = Project.objects.filter(project_type=project_type).order_by('-created_at')

    # Qo'shimcha filterlar (agar kerak bo'lsa)
    year = request.GET.get('year')
    scale = request.GET.get('scale')
    search = request.GET.get('q')

    if year:
        projects = projects.filter(year=year)
    if scale:
        projects = projects.filter(scale__id=scale)
    if search:
        projects = projects.filter(
            Q(title__icontains=search) | 
            Q(description__icontains=search)
        )

    paginator = Paginator(projects, 12)
    page_obj = paginator.get_page(request.GET.get('page'))

    # Statistika
    total_projects = Project.objects.count()
    total_this_year = Project.objects.filter(year=2026).count()
    total_views = Project.objects.aggregate(Sum('views'))['views__sum'] or 0

    context = {
        'project_type': project_type,
        'page_obj': page_obj,
        'project_types': ProjectType.objects.all().order_by('order'),
        'scales': Scale.objects.all(),
        'years': Project.objects.values_list('year', flat=True).distinct().order_by('-year'),
        
        'total_projects': total_projects,
        'total_this_year': total_this_year,
        'total_views': total_views,
    }

    return render(request, 'tip/projects_by_type.html', context)

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q, Sum
from .models import *


def project_typess(request):

    types = ProjectType.objects.all()

    return render(
        request,
        'tip/project_types.html',
        {
            'types': types
        }
    )




def companies(request):

    companies = Company.objects.all().order_by('id')
    sliders = Slider.objects.filter(is_active=True, page='clients').order_by('order')

    context = {
        'companies': companies,
        'sliders': sliders,

    }

    return render(request, 'company/companies.html', context)


def projects_by_type(request, slug):

    project_type = get_object_or_404(
        ProjectType,
        slug=slug
    )
    sliders = Slider.objects.filter(is_active=True, page='project_typesb').order_by('order')

    projects = (
        Project.objects
        .filter(project_type=project_type)
        .order_by('-created_at')
    )

    # FILTERS

    year = request.GET.get('year')
    scale = request.GET.get('scale')
    search = request.GET.get('q')

    if year:
        projects = projects.filter(year=year)

    if scale:
        projects = projects.filter(scale__id=scale)

    if search:
        projects = projects.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search)
        )

    # PAGINATION

    paginator = Paginator(projects, 12)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    # FILTER DATA

    years = (
        Project.objects
        .filter(project_type=project_type)
        .values_list('year', flat=True)
        .distinct()
        .order_by('-year')
    )

    scales = (
        Scale.objects.all()
    )

    # RELATED TYPES

    related_types = (
        ProjectType.objects
        .exclude(id=project_type.id)
        .order_by('order')[:6]
    )
    other_types = ProjectType.objects.exclude(id=project_type.id)
    # STATS

    total_projects = projects.count()
    total_this_year = Project.objects.filter(year=2026).count()
    total_views = (
        projects.aggregate(
            Sum('views')
        )['views__sum'] or 0
    )

    context = {

        'project_type': project_type,
        'other_types': other_types,
        'page_obj': page_obj,
         'sliders': sliders,
        'years': years,

        'scales': scales,

        'related_types': related_types,

        'total_projects': total_projects,

        'total_views': total_views,

        'total_this_year': total_this_year,

        'current_scale': scale,

        'current_search': search,
    }

    return render(
        request,
        'tip/projects_by_type.html',
        context
    )