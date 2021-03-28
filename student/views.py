import datetime
import json
import simplejson
# import pytest

from django.db import models
from django.core import serializers
from django.db.models import F
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.generic import View


from events.models import Event
from projects.models import Project
from leonardo.models import Nyhet
from .models import PrintJob
from .models import Printer
from .utils import PrintQueuesMixin
from .serializers import PrintJobSerializer


def home(request):
    def add_years(years):
        d = datetime.date.today()
        try:
            return d.replace(year=d.year + years)
        except ValueError:
            return d + (datetime.date(d.year + years, 1, 1) - datetime.date(d.year, 1, 1))

    now = timezone.now()
    upcoming = Event.objects.annotate().filter(event_start_time__gte=now)
    nyheter = Nyhet.objects.annotate().filter(post_time__lt=now)

    context = {
        "events": upcoming[0:4],
        'projects': Project.objects.all()[0:6],
        'nyheter': nyheter[0:4],
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

def printer(request):
    context = {
        'user': request.user.id
    }
    return render(request, 'student/printer.html', context)


def terms(request):
    return render(request, 'terms-conditions.html', {})


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)

# Job Handlers

class PrintQueues(PrintQueuesMixin, View):
    def get(self, request):
        data = self.get_relevant_jobs()
        return JsonResponse(data)

class PrintJobClass(PrintQueuesMixin, View):
    def delete(self, request, pk):
        PrintJob.objects.filter(id=pk).delete()
        data = self.get_relevant_jobs()
        return JsonResponse(data)
    def post(self, request):
        # validate user and uniqueness of time slot, recheck that the time slot is available
        date = request.POST.get('date')
        # updated_data = self.get_relevant_jobs()
        return JsonResponse({"queues" : date})
    
class PrintJobRecommendation(PrintQueuesMixin, View):
    def post(self, request):
        duration = request.POST.get('duration')
        queues = self.get_relevant_jobs()
        json_queues = queues['queues']
        
        # json_queues = json.dumps(queues)

        for queue in json_queues:
            queue['proposals'] = self.get_relevant_proposals(queue['jobs'], duration)
            print(queue)


        return JsonResponse({"duration" : duration})