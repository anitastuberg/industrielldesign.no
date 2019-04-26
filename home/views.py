import datetime

from django.shortcuts import render, redirect, get_object_or_404
from events.models import Event
from .models import Styremedlem, Komiteer


def index(request):
    return render(request, 'home/index.html', {})


def about(request):
    context = {
        "styremedlemmer": Styremedlem.objects.all()
    }
    return render(request, 'home/about.html', context)


def students(request):
    def add_years():
        d = datetime.date.today()
        years = 1
        try:
            return d.replace(year=d.year + years)
        except ValueError:
            return d + (datetime.date(d.year + years, 1, 1) - datetime.date(d.year, 1, 1))
    context = {
        "events": Event.objects.filter(event_start_time__range=(datetime.date.today(), add_years()))
    }
    print(context['events'])
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


def terms(request):
    return render(request, 'home/terms-conditions.html', {})
