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

from authentication.models import Profile
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
        newJob = request.POST.get('job')
        jsonObj = json.loads(newJob)

        date = self.get_date_object_for_string(jsonObj['date']) #needs to set with timezone time!!
        duration = jsonObj['duration']
        author = Profile.objects.get(pk=jsonObj['author']) #get username from id?
        print(author.get_username())
        priorities = jsonObj['priority']
        username = "lorentz houser" #jsonObj['username']
        device = jsonObj['device']
        end_delta_time = datetime.timedelta(seconds=int(duration))
        end_date = date+end_delta_time

        PrintJob.objects.create(author=author, print_job_duration=duration, print_job_date=date, print_job_end_date=end_date, username=username, print_job_description="some text for now",print_job_device=device)

        updated_queues = self.get_relevant_jobs()
        return JsonResponse(updated_queues)
    
class PrintJobRecommendation(PrintQueuesMixin, View):
    def post(self, request):
        duration = request.POST.get('duration')
        queues = self.get_relevant_jobs()
        json_queues = queues['queues']

        suggested_startHour = 8
        suggested_endHour = 17
        long_print_constraint = 5*60*60

        #order json queues by number of jobs ascending? 
        earliest_proposal = -1
        earliest_date_obj = -1
        device = -1
        for queue in json_queues:
            proposals = self.get_relevant_proposals(queue['jobs'], duration)
            queue['proposals'] = proposals
            #check if earliest
            date_string = proposals[0]['proposal_start']
            date_obj = self.get_date_object_for_string(date_string)
            if earliest_date_obj == -1 or date_obj < earliest_date_obj:
                device = queue['device']
                earliest_date_obj = date_obj
                earliest_proposal = date_string
    
        
        end_delta_time = datetime.timedelta(seconds=int(duration))
        end_date = earliest_date_obj+end_delta_time
        new_job = {
            'author':1,
            'print_job_date': earliest_proposal,
            'print_job_end_date': end_date,
            'duration': duration,
            'priority': "New",
            'username': "Lorentz Houser",
            'device': device
        }

        for queue in json_queues:
            if queue['device'] == device:
                queue['jobs'].append(new_job)
        
        # recommend first available and from preferably from printer that is not in use

        # send back both updated queues and new job
        # send back the new job with priority = New at the optimal space


        return JsonResponse({
            "queues" : json_queues,
            "new_job": new_job
        })