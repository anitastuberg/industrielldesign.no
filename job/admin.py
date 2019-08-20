from django.contrib import admin

from job.models import Job, Company, JobFilter


class JobAdmin(admin.ModelAdmin):
    list_display = ["__str__", 'deadline']

    class Meta:
        model = Job


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['__str__']

    class Meta:
        model = Company


admin.site.register(Job, JobAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(JobFilter)
