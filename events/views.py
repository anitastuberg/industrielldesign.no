from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied



from .models import Event
from .forms import CreateEventForm

# Create your views here.

def create_event(request):
    # Calls 403 - permission denied if not logged in
    if request.user.is_staff:

        form = CreateEventForm(request.POST or None, request.FILES or None)

        context = {
            'form' : form
        }

        if form.is_valid():
            instance = form.save(commit=False)

            instance.save()
            print(instance.slug)
            return redirect('event', event_slug=instance.slug)
        
        return render(request, 'events/event-creation.html', context)
    else:
        raise PermissionDenied

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



