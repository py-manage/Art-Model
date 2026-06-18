from django.shortcuts import render

# Create your views here.
# team/views.py

from django.shortcuts import render
from .models import Team


def teams(request):

    teams = Team.objects.all()

    return render(
        request,
        'team.html',
        {'teams': teams}
    )