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

def checkClass(user, event):
    isAccess = False

    if user.get_class_year() == 1 and event.class_1:
        isAccess = True
    if user.get_class_year() == 2 and event.class_2:
        isAccess = True
    if user.get_class_year() == 3 and event.class_3:
        isAccess = True
    if user.get_class_year() == 4 and event.class_4:
        isAccess = True
    if user.get_class_year() == 5 and event.class_5:
        isAccess = True
    if user.get_class_year() > 5 and event.alumni:
        isAccess = True
    return isAccess

def stringBuilder(event):
    open_for_string = "Åpent for alle"

    if event.class_1 and event.class_2 and event.class_3 and event.class_4 and event.class_4 and event.class_5 and event.alumni:
        open_for_string = "Åpent for alle IPD-studenter og alumni"
    elif event.class_1 and event.class_2 and event.class_3 and event.class_4 and event.class_4 and event.class_5:
        open_for_string = "Åpent for alle IPD-studenter"
    elif event.class_3 and event.class_4 and event.class_4 and event.class_5:
        open_for_string = "Åpent for 3. - 5. klasse"
    elif event.class_1 and event.class_2:
        open_for_string = "Åpent for 1. og 2. klasse"
    elif event.class_4 and event.class_5:
        open_for_string = "Åpent for 4. og 5. klasse"
    elif event.class_1:
        open_for_string = "Åpent for 1. klassse"
    elif event.class_2:
        open_for_string = "Åpent for 2. klassse"
    elif event.class_3:
        open_for_string = "Åpent for 3. klassse"
    elif event.class_4:
        open_for_string = "Åpent for 4. klassse"
    elif event.class_5:
        open_for_string = "Åpent for 5. klassse"
    else:
        open_for_string = "Åpent for noen"
    
    return open_for_string

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
        open_for_string = stringBuilder(event);

        
        context['already_registered'] = already_registered
        context['open_for'] = open_for_string
        context['no_access'] = False
        context['not_open_yet'] = True
        context['waiting_list'] = False
        context['event_not_full'] = False
        context['only_komite'] = event.only_komite

        response_data = {
            "loginSuccess" : "False",
            'no_access': False,
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
            if not checkClass(user, event):
                context['no_access'] = True

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

                    if (event.registration_required) and (not checkClass(user, event)):
                        response_data['no_access'] = True
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
                komite_open = True
                if (event.only_komite and not user.is_komite):
                    komite_open = False
                if (event.registration_required) and (checkClass(user, event)) and (event.registration_start_time <= timezone.now()) and (context['event_not_full'] and (komite_open)):
                    event.registered_users.add(user)
                    print("%s %s: %s" % (user.first_name, user.last_name, timezone.now()))
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
