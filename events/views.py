from django.shortcuts import render, redirect

from .models import Event

# Create your views here.

def create_event(request):
    if user.groups.filter(name="event_maker").exists():
        return render(request, 'events/event-creation.html', {})

def event(request, event_number):

    event = Event.objects.get(pk=event_number)

    if request.method == 'GET':

        context = {
            'event': event
        }

        return render(request, 'events/event-page.html', context)
    
    else:
        event.registered_users.add(request.user)
        return redirect('students')



