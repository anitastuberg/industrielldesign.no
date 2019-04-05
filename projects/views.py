from django.shortcuts import render, redirect
from django.http import JsonResponse

from projects.forms import CreateProjectForm
from .models import Project, ProjectImage


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


def create_project(request):
    context = {
        'form': CreateProjectForm()
    }
    if request.method == 'GET':
        return render(request, 'projects/create-project.html', context)
    else:
        form = CreateProjectForm(request.POST, request.FILES or None)
        context['form'] = form
        if form.is_valid() and len(request.FILES.getlist('images')) <= 10:
            project = form.save(commit=False)
            files = request.FILES.getlist('images')
            project.save()

            try:
                for f in files:
                    ProjectImage.objects.create(image=f, project=project)
            except:
                project.delete()
                return render(request, 'apartments/create-apartment.html', context)
            return redirect('projects')
        else:
            return render(request, 'apartments/create-apartment.html')