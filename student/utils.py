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
            # now_string_format = timezone.now()
            # iso 8601
            # string_date = json.dumps(datetime.now().isoformat("T", "milliseconds"), default=str)
            string_date = json.dumps(datetime.now(timezone.utc).astimezone().isoformat(sep="T", timespec="seconds"), default=str)
            
            # now_string_format = now#.strftime('YYYY-MM-DDTHH:MM:SS+HH:MM')
            proposals = ({'proposal_start' : string_date, 'proposal_end' : -1})
            return proposals
        elif (len(sorted_jobs) == 1):
            print('yes')
            start = sorted_jobs[0]['print_job_end_date']
            proposals = ({'proposal_start' : start, 'proposal_end' : -1})
            return proposals
        else:
            proposals = []
            print(len(sorted_jobs))
            for i in range(0,len(sorted_jobs)-1):
                if (i == len(sorted_jobs)-1):
                    proposal = ({'proposal_start' : current, 'proposal_end' : next})
                    proposals.append(sorted_jobs[i]['print_job_end_date'])
                # elif (i==0):
                    # possible job before first 
                else:
                    next = sorted_jobs[i+1]['print_job_date']
                    current = sorted_jobs[i]['print_job_end_date']
                    # parse time seconds delta from ^
                    # if duration <= datetime.strptime(next, '%y-%m-%d%h:%m:%s:')-datetime.strptime(current, '%y-%m-%d%h:%m:%s:'):
                    # next_date = next.split('T')

                    # %Y-%m-%d %H:%M:%S.%f'
                    #.split('+')[0]
                    next_parts = next.split("T")
                    next = next_parts[0] + " " + next_parts[1][0:8] 
                    print(next)

                    current_parts = current.split("T")
                    current = current_parts[0] + " " + current_parts[1][0:8] 
                    print(current)

                    # current = '2018-06-29 10:15:27'
                    next_obj = datetime.strptime(next, '%Y-%m-%d %H:%M:%S')
                    current_obj = datetime.strptime(current, '%Y-%m-%d %H:%M:%S')
                    delta = (next_obj-current_obj).total_seconds()
                    # delta_hms = delta.split(':')
                    # delta_seconds = delta_hms[0]*3600 + delta_hms[1]*60 + delta_hms[2]
                    print("delta time")
                    print(delta)

                    if duration <= delta:
                        # proposal = ({'proposal_start' : current, 'proposal_end' : next})
                        # proposals.append(proposal)
            return []

    

