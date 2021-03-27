from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .serializers import PrintJobSerializer
from .models import *
from django.utils import timezone

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
            jobQuerySet = self.print_job_model.objects.annotate().filter(print_job_end_date__gte=now).filter(print_job_device=int(printer))
            jobs = PrintJobSerializer(jobQuerySet, many=True).data
            queues.append({ 'device': printer, 'jobs': jobs})

        data={ 
            'queues': queues
        }
        return data
