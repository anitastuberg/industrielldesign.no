from django.contrib import admin

from .models import Project
from .forms import CreateProjectForm

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    form = CreateProjectForm
    # ordering = ('creation_date',)

    class Meta:
        model = Project

admin.site.register(Project, ProjectAdmin)