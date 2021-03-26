from django.contrib import admin

from .models import Printer, PrintJob, PriorityFilter


# Register your models here.
class PrintJobAdmin(admin.ModelAdmin):
    # ordering = ('creation_date')
    class Meta:
        model = PrintJob


admin.site.register(PrintJob, PrintJobAdmin)
admin.site.register(PriorityFilter)
admin.site.register(Printer)