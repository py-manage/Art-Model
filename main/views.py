
from django.shortcuts import render, get_object_or_404
from .models import Project, MockupType, Client

def home(request):
    """ Bosh sahifa: Oxirgi loyihalar va mijozlar ro'yxati """
    latest_projects = Project.objects.all()[:6] # Oxirgi 6 ta loyiha
    clients = Client.objects.all()
    
    context = {
        'projects': latest_projects,
        'clients': clients,
    }
    return render(request, 'index.html', context)

def mockup_type_detail(request, slug):
    """ Maket turiga bosganda, faqat shu turdagi loyihalarni ko'rsatish """
    mockup_type = get_object_or_404(MockupType, slug=slug)
    projects = mockup_type.projects.all() # related_name orqali filtrlaymiz
    
    context = {
        'mockup_type': mockup_type,
        'projects': projects,
    }
    return render(request, 'portfolio/mockup_type.html', context)

def project_detail(request, slug):
    """ Loyihaning ichki batafsil sahifasi """
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'portfolio/project_detail.html', {'project': project})


def project(request):
    return render(request,'project.html')

def projectd(request):
    return render(request,'project-details.html')

def team(request):
    return render(request,'team.html')

def teamd(request):
    return render(request,'team-details.html')

def about(request):
    """ O studii / Biz haqimizda sahifasi """
    return render(request, 'about.html')

def contact(request):
    """ Kontaktlar sahifasi """
    return render(request, 'contact.html')

def service(request):
    return render(request,"service.html")
    
def serviced(request):
    return render(request,"service-detailes.html")

def blog(request):
    return render(request,"news-grid.html")

def blogd(request):
    return render(request,"news-details.html")