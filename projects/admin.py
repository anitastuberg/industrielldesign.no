from django.contrib import admin

from .models import Project, ProjectImage
from .forms import CreateProjectForm


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'course', 'year', 'semester']
    form = CreateProjectForm
    # ordering = ('creation_date',)

    class Meta:
        model = Project


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)