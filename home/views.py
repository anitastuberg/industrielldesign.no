from django.shortcuts import render, redirect, get_object_or_404
from events.models import Event

def index(request):
    return render(request, 'home/index.html', {})

def about(request):
    return render(request, 'home/about.html', {})

def students(request):

    context = {
        "events": Event.objects.all()
    }

    return render(request, 'home/students.html', context)

def snake(request):
    return render(request, 'testing/404/404.html', {})

def page_not_found(request):
    return render(request, '404.html')