from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .serializers import PrintJobSerializer
from .models import *
from django.utils import timezone
from datetime import datetime
import json


class PrintQueuesMixin(object):
    print_job_model = PrintJob
    printer_model = Printer

    def get_relevant_jobs(self):
        printers = self.printer_model.objects.all()
        # get_object_or_404 ?
        printerNames = []
        for printer in printers:
            printerNames.append(printer.name)

        now = timezone.now()
        queues = []

        for printer in printerNames:
            # serialize queryset
            # filter such that end of job is > now
            jobQuerySet = self.print_job_model.objects.annotate().filter(print_job_end_date__gte=now).filter(print_job_device=int(printer)).order_by('print_job_date')
            jobs = PrintJobSerializer(jobQuerySet, many=True).data
            queues.append({ 'device': printer, 'jobs': jobs })

        data={ 
            'queues': queues
        }
        return data

    
    
    def get_relevant_proposals(self, sorted_jobs, duration):
        # value = "relevant_proposals"
        if (len(sorted_jobs) == 0):
            # round up time?
            # iso 8601
            now_string_date = json.dumps(datetime.now(timezone.utc).astimezone().isoformat(sep="T", timespec="seconds"), default=str)
            # now_string_format = now#.strftime('YYYY-MM-DDTHH:MM:SS+HH:MM')
            proposals = ({'proposal_start' : now_string_date, 'proposal_end' : -1})
            return proposals
        else:
            proposals = []
            now = datetime.now()

            now_string_date = json.dumps(datetime.now(timezone.utc).astimezone().isoformat(sep="T", timespec="seconds"), default=str)
            first_job_start = sorted_jobs[0]['print_job_date']
            first_parts = first_job_start.split("T")
            first_job_start_string = first_parts[0] + " " + first_parts[1][0:8] 
            first_job_date_obj = datetime.strptime(first_job_start_string, '%Y-%m-%d %H:%M:%S')
            delta = (first_job_date_obj - now).total_seconds()
            if  delta > int(duration) and delta > 0:
                # Adds proposal before first job if possible
                print("space before first job")
                proposal = {'proposal_start' : now_string_date, 'proposal_end' : first_job_start}
                proposals.append(proposal)

            if (len(sorted_jobs) > 1):
                # Adds proposals between existing jobs 
                print('more than one current job')
                for i in range(0,len(sorted_jobs)-1):
                    next = sorted_jobs[i+1]['print_job_date']
                    current = sorted_jobs[i]['print_job_end_date']
                    # parse time seconds delta from ^

                    # reconstructing the string formatted dates
                    next_parts = next.split("T")
                    next = next_parts[0] + " " + next_parts[1][0:8] 
                    print(next)

                    current_parts = current.split("T")
                    current = current_parts[0] + " " + current_parts[1][0:8] 
                    print(current)

                    next_obj = datetime.strptime(next, '%Y-%m-%d %H:%M:%S')
                    current_obj = datetime.strptime(current, '%Y-%m-%d %H:%M:%S')
                    delta = (next_obj-current_obj).total_seconds()

                    if int(duration) <= int(delta):
                        proposal = {'proposal_start' : current, 'proposal_end' : next}
                        proposals.append(proposal)
            # always add a proposal after the the end of the last job
            last_job_start_date = sorted_jobs[-1]['print_job_end_date']
            proposal = {'proposal_start' : last_job_start_date, 'proposal_end' : -1}
            proposals.append(proposal)
            return proposals

    

