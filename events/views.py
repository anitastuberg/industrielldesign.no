from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
# from django.utils import simplejson



from .models import Event
from .forms import CreateEventForm

# Create your views here.

def create_event(request):
    # Calls 403 - permission denied if not logged in
    if user.is_staff:

        form = CreateEventForm(request.POST or None, request.FILES or None)

        context = {
            'form' : form
        }

        if form.is_valid():
            instance = form.save(commit=False)
            image = form.cleaned_data['image']
            instance.save()
            return redirect('event', event_slug=instance.slug)
        
        return render(request, 'events/event-creation.html', context)
    else:
        raise PermissionDenied

def event(request, event_slug):

    user = request.user

    event = Event.objects.get(slug=event_slug)
    register_users_count = event.registered_users.all().count()
    already_registered =  user in event.registered_users.all()

    context = {
        'event': event,
        'already_registered': already_registered
    }

    response_data = {
        "success" : "False"
    }
    
    # If registering
    if event.available_spots is not None:
        event_not_full = register_users_count < event.available_spots
        context.update({
            'event_not_full': event_not_full,
            'event_registration': True
        })
        response_data["event_not_full"] = event_not_full

    

    if request.method == 'GET':

        return render(request, 'events/event-page.html', context)
    
    else: # POST
        # If already signed up users count is less than available spots
        if not user.is_authenticated:
            
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                login(request, user)
                already_registered =  user in event.registered_users.all()

                response_data['success'] = True
                response_data['already_registered'] = already_registered
                response_data['first_name'] = user.first_name
                response_data['allergies'] = user.allergies
            else:
                response_data['success'] = False
                
        if not request.POST.get('email'):

            if event_not_full:
                event.registered_users.add(user)
                response_data['success'] = True
                response_data['already_registered'] = True
                
            else:
                pass
            
        return JsonResponse(response_data)

