from django.shortcuts import render
from django.http import JsonResponse

from .models import Project

# Create your views here.
def projects(request):
    # GET
    # Returns all projects in the database to be displayed on the project front page
    if request.method == 'GET':
        context = {
            "projects": Project.objects.all()
        }
        return render(request, 'projects/projects.html', context)

    # POST
    # Pressing a project will send back detailed data for that project to be displayed
    # in the project detail modal.
    else:
        slug = request.POST.get('slug')
        project = Project.objects.get(slug=slug)
        response_data = {
            'project_title': project.title,
            'project_description': project.description,
            'project_image': project.thumbnail.url,
            'project_creator': project.creator,
            'project_course': project.course,
            'project_year': project.year,
            'project_semester': project.semester
        }

        return JsonResponse(response_data)