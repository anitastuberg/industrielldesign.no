from django.urls import path

from . import views

urlpatterns = [
    path('designsystem', views.design_system, name="designsystem")
]