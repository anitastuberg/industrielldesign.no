from django.urls import path

from . import views

urlpatterns = [
    path('arrangementer/nytt-arrangement', views.create_event, name="create_event"),
    path('arrangementer', views.all_events, name="all_events"),
    path('arrangementer/<slug:event_slug>', views.event, name="event"),
    path('arrangementer/<slug:event_slug>/admin', views.event_admin, name="event_admin"),
]