from django.urls import path

from . import views

urlpatterns = [
    path('event/create', views.create_event, name="create_event"),
    path('event/<slug:event_slug>', views.event, name="event"),
    path('event/<slug:event_slug>/admin', views.event_admin, name="event_admin"),
]