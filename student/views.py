import datetime

from django.db import models
from django.db.models import F
from django.shortcuts import render
from django.utils import timezone

from events.models import Event
from projects.models import Project


def home(request):
    def add_years(years):
        d = datetime.date.today()
        try:
            return d.replace(year=d.year + years)
        except ValueError:
            return d + (datetime.date(d.year + years, 1, 1) - datetime.date(d.year, 1, 1))

    now = timezone.now()
    upcoming = Event.objects.annotate().filter(event_start_time__gte=now)

    context = {
        "events": upcoming[0:4],
        'projects': Project.objects.all()[0:6]
    }
    return render(request, 'index.html', context)


# STUDENT
def student(request):
    return render(request, 'student/student.html')


def klassetur(request):
    return render(request, 'student/klassetur.html')


def utveksling(request):
    return render(request, 'student/utveksling.html')


def ny_student(request):
    return render(request, 'student/ny-student.html')


def terms(request):
    return render(request, 'terms-conditions.html', {})


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
