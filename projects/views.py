from django.shortcuts import render

# Create your views here.
def projects(request):
    return render(request, 'projects/projects.html', {})

def project_details(request, project_slug):
    project = Projects.get(slug=project_slug)
    
    context = {
        "project": project,
    }
