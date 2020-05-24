from django.shortcuts import render
from .models import Project
from django.http import HttpResponse

def homepage(request):
    projects = Project.objects.all()
    return render(request, 'pages/home.html/', {'projects': projects})



