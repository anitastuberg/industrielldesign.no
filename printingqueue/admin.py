from django.contrib import admin

from .models import Printjob, Printer

# Register your models here.
admin.site.register(Printer)
admin.site.register(Printjob)