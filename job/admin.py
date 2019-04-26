from django.contrib import admin

from job.models import Job


class JobAdmin(admin.ModelAdmin):
    list_display = ["__str__", 'deadline']

    class Meta:
        model = Job


admin.site.register(Job, JobAdmin)