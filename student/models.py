from django.db import models
from django.conf import settings

import datetime

class Printer(models.Model):
    name = models.CharField(max_length=20, unique=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class PriorityFilter(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
class PrintJob(models.Model):
    print_job_date = models.DateTimeField(auto_now=False)
    print_job_end_date = models.DateTimeField(auto_now=False)
    print_job_duration = models.BigIntegerField()
    print_job_device = models.IntegerField()
    
    priorities = models.ManyToManyField(PriorityFilter)
        # user: userId

    # jobUser = models.IntegerField()

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    username = models.CharField(max_length=200, blank=True)

    print_job_description = models.CharField(max_length=200, null=True, blank=True)
    