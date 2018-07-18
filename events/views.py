from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
# from django.utils import simplejson



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
            image = form.cleaned_data['image']
            instance.save()
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
    
    else: # POST
        # If already signed up users count is less than available spots
        if event_not_full:
            event.registered_users.add(request.user)
            return redirect('students')
        else:
            pass

def event_login(request):
    xhr = request.GET.has_key('xhr') # True if Ajax request

    # If request method is POST
    if request.method == 'POST':
        # Returns new data if request is ajax and user is authenticated
        if xhr and request.user.is_authenticated:
            # Data to send back
            response_dict = {
                'Fornavn': request.user.first_name,
                'Allergier': request.user.allergies
                }
            # Sends the data as JSON
            return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')

        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
        
        return HttpResponse('')

