from django.urls import path
from django.conf import settings
from django.contrib.auth.views import logout

from . import views

urlpatterns = [
    path('prosjekter/', views.projects, name="projects"),
    path('opprett-prosjekt/', views.create_project, name="create-project"),
    path('prosjekter/<slug:project_slug>', views.project_detail, name="project-detail")
]