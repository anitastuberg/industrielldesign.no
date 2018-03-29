from django.shortcuts import render

# from .models import Event

# Create your views here.

def create_event(request):
    if user.groups.filter(name="event_maker").exists():
        return render(request, 'events/event-creation.html', {})

def event(request, event_number):

    context = {
        'event': Event.objects.get(pk=event_number)
    }

    return render(request, 'events/event-page.html', context)
