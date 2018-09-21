from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
# from django.utils import simplejson
from django.utils import timezone



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
    # user.update_class_year() # Updates user to alumni if old enough
    event = Event.objects.get(slug=event_slug)
    event.update_waiting_list()

    context = {
        'event': event
    }
    if event.registration_required:

        register_users_count = event.registered_users.all().count()
        already_registered =  user in event.registered_users.all()
        waiting_list = event.available_spots is not None

        # Creates a string to post on event-page. "Åpent for 3. - 5.klasse" or "Åpent for alle" if registration is required
        if event.registration_year_limit and event.registration_year_limit < 5000: # Not open for alumni
            open_for_string = "Åpent for %d. - 5. klasse" % (5 - (event.get_class_year(event.registration_year_limit)))
        else:
            open_for_string = "Åpent for Alle"

        
        context['already_registered'] = already_registered
        context['open_for'] = open_for_string
        context['too_young'] = False
        context['not_open_yet'] = True
        context['waiting_list'] = False
        context['event_not_full'] = False
        context['only_komite'] = event.only_komite

        response_data = {
            "loginSuccess" : "False",
            'too_young': False,
            'not_open_yet': event.registration_start_time >= timezone.now(),
            'open_for': open_for_string,
            'only_komite': False
        }

        # Check if event is full
        if event.available_spots is not None:
            if register_users_count < event.available_spots:
                context['event_not_full'] = True
            else:
                context['waiting_list'] = True
                response_data['waiting_list'] = waiting_list
        else: 
            context['event_not_full'] = True
        
        # Check age of user
        if (user.is_authenticated):
            print(user.graduation_year)
            if (user.graduation_year > event.registration_year_limit):
                context['too_young'] = True

        # Check if registration has opened
        if event.registration_start_time <= timezone.now():
            context['not_open_yet'] = False

        if user in event.waiting_list.all():
            context['on_waiting_list'] = True

    if request.method == 'GET':

        return render(request, 'events/event-page.html', context)
    
    else: # POST
        if (event.registration_required):
            # If user is not logged in this request is the login-request
            if not user.is_authenticated:
                
                email = request.POST.get('email')
                password = request.POST.get('password')

                user = authenticate(request, email=email, password=password)
                
                # If user exists
                if user is not None:
                    login(request, user) # Log in user
                    already_registered =  user in event.registered_users.all() # Update "already registered" with the new user

                    if (event.registration_required) and (user.graduation_year > event.registration_year_limit):
                        response_data['too_young'] = True
                    # Sends data through ajax to eventpage. Is inserted with js client-side
                    response_data["event_not_full"] = context['event_not_full']
                    response_data['loginSuccess'] = True # Log in succesful
                    response_data['already_registered'] = already_registered
                    response_data['only_komite'] = context['only_komite']
                    response_data['first_name'] = user.first_name
                    response_data['allergies'] = user.allergies
                else:
                    response_data['loginSuccess'] = False # User does not exist
                    
            elif not request.POST.get('email'): # If request doesn't contain an email. It is a sign-up request
                print(request.POST.get('waiting_list'))
                komite_open = True
                if (event.only_komite and not user.is_komite):
                    komite_open = False
                if (event.registration_required) and (user.graduation_year < event.registration_year_limit) and (event.registration_start_time <= timezone.now()) and (context['event_not_full'] and (komite_open)):
                    event.registered_users.add(user)
                    response_data['registerSuccess'] = True
                    response_data['already_registered'] = True
                # Check if waiting list was pressed
                elif request.POST.get('waiting_list') == "true":
                    event.waiting_list.add(user)
                    response_data["on_waiting_list"] = True
                else:
                    response_data['registerSuccess'] = False
                
            return JsonResponse(response_data)
        else:
            pass


def event_admin(request, event_slug):
    event = Event.objects.get(slug=event_slug)
    context = {"event": event}

    if (request.user.is_staff):
        return render(request, 'events/event-admin.html', context)
    else:
        raise PermissionDenied
