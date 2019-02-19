from django.shortcuts import render, redirect, get_object_or_404
from events.models import Event
from .models import Styremedlem, Komiteer, Jobb

def index(request):
    return render(request, 'home/index.html', {})

def about(request):
    context = {
        "styremedlemmer": Styremedlem.objects.all()
    }
    return render(request, 'home/about.html', context)

def students(request):
    context = {
        "januar": Event.objects.all().filter(event_start_time__month=1).order_by('event_start_time'),
        "februar": Event.objects.all().filter(event_start_time__month=2).order_by('event_start_time'),
        "mars": Event.objects.all().filter(event_start_time__month=3).order_by('event_start_time'),
        "april": Event.objects.all().filter(event_start_time__month=4).order_by('event_start_time'),
        "mai": Event.objects.all().filter(event_start_time__month=5).order_by('event_start_time'),
        "juni": Event.objects.all().filter(event_start_time__month=6).order_by('event_start_time'),
        "juli": Event.objects.all().filter(event_start_time__month=7).order_by('event_start_time'),
        "august": Event.objects.all().filter(event_start_time__month=8).order_by('event_start_time'),
        "september": Event.objects.all().filter(event_start_time__month=9).order_by('event_start_time'),
        "oktober": Event.objects.all().filter(event_start_time__month=10).order_by('event_start_time'),
        "november": Event.objects.all().filter(event_start_time__month=11).order_by('event_start_time'),
        "desember": Event.objects.all().filter(event_start_time__month=12).order_by('event_start_time')
    }
    return render(request, 'home/students.html', context)

def snake(request):
    return render(request, 'testing/404/404.html', {})

def page_not_found(request):
    return render(request, '404.html')

def komiteer(request):
    context = {
        'komiteer': Komiteer.objects.all()
    }
    return render(request, 'home/komiteer.html', context)

# Andy:
def jobb(request):
    context = {
        'Stillingsannonser': Jobb.objects.all()
    }
    return render(request, 'home/jobb.html', context)
