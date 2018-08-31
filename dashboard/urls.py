from django.urls import path
from django.conf import settings

from . import views

urlpatterns = [
    path('event/<slug:event_slug>/admin', views.eventAdmin, name="event_admin"),
]