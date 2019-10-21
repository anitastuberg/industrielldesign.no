from django.contrib import admin

from .models import Printer, Job

# Register your models here.
admin.site.register(Printer)
admin.site.register(Job)
