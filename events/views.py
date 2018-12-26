from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings



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

def updateButtonEventButton(user, event):
    buttonText = 'Bli med'
    buttonState = True
    if event.available_spots is not None:
        if event.registered_users.all().count() >= event.available_spots:
            buttonText = "Legg deg i ventelisten"
            buttonState = True
    # If user is logged in
    if user.is_authenticated:
        # Check if in correct class
        if not checkClass(user, event):
            buttonText = "Ikke tilgang"
            buttonState = False
        # If on waitinglist
        elif user in event.waiting_list.all():
            buttonText = "Du står på venteliste"
            buttonState = False
        elif not user.is_komite and event.only_komite:
            buttonText = "Bare for komitéer"
            buttonState = False
    if event.registration_start_time <= timezone.now():
        buttonText = "Påmelding ikke åpnet enda"
        buttonState = False

    return buttonText, buttonState


def event(request, event_slug):

    user = request.user
    # user.update_class_year() # Updates user to alumni if old enough
    event = Event.objects.get(slug=event_slug)
    # Whenever someone enters the event page. Waiting list is updated
    event.update_waiting_list()
    # Generates a string based on who the event is open for
    open_for_string = stringBuilder(event);

    # On load data
    context = {
        'buttonText': '',
        'buttonState': False,
        'open_for' = open_for_string,
        'not_open_yet' = True,
        'loginSuccess' = False,
        'user' = user,
    }

    # Check if registration has opened
    if event.registration_start_time <= timezone.now():
        context['not_open_yet'] = False

    context['buttonText'], context['buttonState'] = updateButtonEventButton(user, evnet)
    
    #### HTTP Part ####
    # GET (On page load)
    if request.method == 'GET':
        return render(request, 'events/event-page.html', context)
    
    # POST (User sending data) requests are only nescescarry if event
    # has registration
    elif request.method == 'POST' and event.registration_required:
        if not user.is_authenticated:
            email = request.POST.get('email') # Get username/email
            password = request.POST.get('password') # Get password

            # Retrieves the user
            user = authenticate(request, email=email, password=password)

            # If user exists
            if user is not None:
                login(request, user)
                context['user'] = user
                context['loginSuccess'] = True
                context['buttonText'], context['buttonState'] = updateButtonEventButton(user, evnet)
            # If user does not exist
            else:
                response_data['loginSuccess'] = False
        
        elif not request.POST.get('email') # If request doesn't contain an email. It is a sign-up request
            if (event.registration_required) and (checkClass(user, event)) and (event.registration_start_time <= timezone.now()) and (context['event_not_full'] and (event.only_komite and user.is_komite)):
                event.registered_users.add(user)
                context['registerSuccess'] = True
                context['buttonText'], context['buttonState'] = updateButtonEventButton(user, evnet)
            elif request.POST.get('waiting_list') == 'true':
                event.waiting_list.add(user)
                context['buttonText'], context['buttonState'] = updateButtonEventButton(user, evnet)
            else:
                context['registerSuccess'] = False
        return JsonResponse(context)



def event_admin(request, event_slug):
    event = Event.objects.get(slug=event_slug)
    context = {"event": event}

    if (request.user.is_staff):
        return render(request, 'events/event-admin.html', context)
    else:
        raise PermissionDenied

def send_event_confirmation_mail(subject, message, user_email):
    send_mail(
        subject, # Subject
        message, # Message
        settings.EMAIL_HOST_USER, # From email
        [user_email], # To email
        fail_silently=False,
    )