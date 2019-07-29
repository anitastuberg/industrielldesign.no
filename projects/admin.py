from django.contrib import admin

from .models import Project, ProjectImage
from .forms import CreateProjectForm


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['pk', 'course', 'creator', 'class_year', 'creation_date']
    fields = ['description', 'creator', 'class_year', 'course' ]
    # ordering = ('creation_date',)

    class Meta:
        model = Project


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)