import datetime

from django.db import models
from django.db.models import F
from django.shortcuts import render
from django.utils import timezone

from events.models import Event
from .models import Styremedlem, Komiteer, TheSign
from projects.models import Project


def home(request):
    def add_years(years):
        d = datetime.date.today()
        try:
            return d.replace(year=d.year + years)
        except ValueError:
            return d + (datetime.date(d.year + years, 1, 1) - datetime.date(d.year, 1, 1))

    now = timezone.now()
    events = (Event.objects.annotate(
        relevance=models.Case(
            models.When(event_start_time__gte=now, then=1),
            models.When(event_start_time__lt=now, then=2),
            output_field=models.IntegerField(),
        )).annotate(
        timediff=models.Case(
            models.When(event_start_time__gte=now, then=F('event_start_time') - now),
            models.When(event_start_time__lt=now, then=now - F('event_start_time')),
            output_field=models.DurationField(),
        )).order_by('relevance', 'timediff'))

    context = {
        "events": events[0:4],
        'projects': Project.objects.all()[0:7]
    }
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


def komite_detail(request, komite_pk):
    context = {
        'komite': Komiteer.objects.get(pk=komite_pk)
    }
    return render(request, 'home/leonardo/komite-details.html', context)


def terms(request):
    return render(request, 'home/terms-conditions.html', {})
