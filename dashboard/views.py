from django.shortcuts import render
from django.http import HttpResponseForbidden

from events.models import Event

# Create your views here.
def eventAdmin(request, event_slug):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    else:
        event = Event.objects.get(slug=event_slug)

        context = {'event': event}

        return render(request, 'events/event-admin.html', context)