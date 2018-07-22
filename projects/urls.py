from django.urls import path
from django.conf import settings
from django.contrib.auth.views import logout

from . import views

urlpatterns = [
    path('projects/', views.projects, name="projects"),
    path('event/<slug:project_slug>', views.project_details, name="project-detail")
]