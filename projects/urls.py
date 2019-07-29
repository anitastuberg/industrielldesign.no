from django.urls import path

from . import views

urlpatterns = [
    path('prosjekter/', views.projects, name="projects"),
    path('prosjekter/opprett-prosjekt/', views.create_project, name="create_project"),
    path('api/prosjekter/lagre-bilde/', views.upload_project_image, name="upload_project_image"),
    path('api/prosjekter/slett-bilde/', views.remove_project_image, name="remove_project_image"),
    path('api/prosjekter/slett-prosjekt/', views.delete_project, name="delete_project"),
    path('prosjekter/<int:project_pk>', views.project_detail, name="project_detail")
]