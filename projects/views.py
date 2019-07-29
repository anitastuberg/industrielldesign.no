from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse

from projects.forms import CreateProjectForm
from .models import Project, ProjectImage


# Create your views here.
def projects(request):
    context = {
        "projects": Project.objects.exclude(creator__isnull=True)
    }
    return render(request, 'projects/projects.html', context)

def create_initial_project(request):
    project = Project.objects.create()
    return HttpResponse(project.pk)


def remove_project_image(request):
    filename = request.POST.get('filename')
    project = request.POST.get('project_pk')
    try:
        project_image = ProjectImage.objects.get(name=filename)
        if project_image.project.pk == project:
            project_image.delete()
            return HttpResponse(status=200)
        return HttpResponse(status=403)
    except ProjectImage.DoesNotExist:
        return HttpResponse(status=404)


def upload_project_image(request):
    try:
        pk = request.POST.get('project_pk')
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return HttpResponse("Project does not exist")

    uploaded_file = request.FILES['file']
    ProjectImage.objects.create(image=uploaded_file, project=project, name=uploaded_file.name)
    return HttpResponse("File uploaded")


def delete_project(request):
    pk = request.POST.get('pk')
    try:
        project = Project.objects.get(pk=pk)
        if not project.creator and project:
            project.delete()
        return HttpResponse(status=200)
    except Project.DoesNotExist:
        return HttpResponse(status=404)


def create_project(request):
    context = {
        'form': CreateProjectForm()
    }
    if request.method == 'GET':
        return render(request, 'projects/create-project.html', context)
    else:
        project_pk = request.POST.get('project_pk')
        try:
            project = Project.objects.get(pk=project_pk)
            form = CreateProjectForm(request.POST, instance=project)
            print(request.POST)
            context['form'] = form
            if form.is_valid():
                project = form.save(commit=False)
                project.save()
                return JsonResponse({'pk': project.pk})
            else:
                print(form.errors)
                return HttpResponse('error')
        except Project.DoesNotExist:
            project = Project.objects.create()
            return JsonResponse({'pk': project.pk})


def project_detail(request, project_pk):
    context = {
        'project': Project.objects.get(pk=project_pk)
    }
    if request.method == 'GET':
        return render(request, 'projects/project-detail.html', context)