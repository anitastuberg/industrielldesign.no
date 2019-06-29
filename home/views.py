import datetime

from django.shortcuts import render, redirect, get_object_or_404
from events.models import Event
from .models import Styremedlem, Komiteer, TheSign


def home(request):
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
    return render(request, 'home/index.html', context)


def leonardo(request):
    return render(request, 'home/leonardo/leonardo.html')


def leonardo_shop(request):
    return render(request, 'home/leonardo/leo-shop.html')


def thesign(request):
    context = {
        'thesigns': TheSign.objects.all
    }
    return render(request, 'home/leonardo/theSign.html', context)


# STUDENT
def student(request):
    return render(request, 'home/student/student.html')


def klassetur(request):
    return render(request, 'home/student/klassetur.html')


def utveksling(request):
    return render(request, 'home/student/utveksling.html')


def ny_student(request):
    return render(request, 'home/student/ny-student.html')


def about(request):
    context = {
        "styremedlemmer": Styremedlem.objects.all()
    }
    return render(request, 'home/leonardo/about.html', context)


def snake(request):
    return render(request, 'testing/404/404.html', {})


def page_not_found(request):
    return render(request, '404.html')


def komiteer(request):
    context = {
        'komiteer': Komiteer.objects.all()
    }
    return render(request, 'home/leonardo/komiteer.html', context)


def terms(request):
    return render(request, 'home/terms-conditions.html', {})
