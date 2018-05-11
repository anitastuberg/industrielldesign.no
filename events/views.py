from django.shortcuts import render, redirect
from django.contrib.auth.models import User


from .models import Event

# Create your views here.

def create_event(request):
    if user.groups.filter(name="event_maker").exists():
        return render(request, 'events/event-creation.html', {})

def event(request, event_slug):

    event = Event.objects.get(slug=event_slug)
    register_users_count = event.registered_users.all().count()
    already_registered =  request.user in event.registered_users.all()

    context = {
        'event': event,
        'already_registered': already_registered
    }
    # If registering
    if event.available_spots is not None:
        event_not_full = register_users_count < event.available_spots
        context.update({
            'event_not_full': event_not_full,
            'event_registration': True
        })

    if request.method == 'GET':

        return render(request, 'events/event-page.html', context)
    
    else:
        
        # If already signed up users count is less than available spots
        if event_not_full:
            event.registered_users.add(request.user)
            return redirect('students')
        else:
            pass



