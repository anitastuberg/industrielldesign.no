
from django.urls import path

from . import views

urlpatterns = [
    path('queues/3d-print', views.printing, name="3d_print"),
]
