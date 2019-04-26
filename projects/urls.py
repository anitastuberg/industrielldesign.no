from django.urls import path
from django.conf import settings
from django.contrib.auth.views import logout

from . import views

urlpatterns = [
    path('projects/', views.projects, name="projects"),
    path('create-project/', views.create_project, name="create-project"),
]