from django.urls import path

from . import views

urlpatterns = [
    path('prosjekter/', views.projects, name="projects"),
    path('opprett-prosjekt/', views.create_project, name="create-project"),
    path('prosjekter/<slug:project_slug>', views.project_detail, name="project-detail")
]