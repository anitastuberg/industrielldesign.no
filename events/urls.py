from django.urls import path
from django.conf import settings
from django.contrib.auth.views import logout

from . import views

urlpatterns = [
    path('event/create-new', views.create_event, name="create_event"),
    path('event/<int:event_number>', views.event, name="event")
]