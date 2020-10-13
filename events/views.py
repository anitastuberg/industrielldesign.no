import datetime

from django.db import models
from django.db.models import F
from django.db.models import Case, CharField, Value, When
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings

from .models import Event
from .forms import CreateEventForm


# Create your views here.

def all_events(request):
    now = timezone.now()
    upcoming = Event.objects.annotate().filter(event_start_time__gte=now) #kommende events, er sortert etter dato i database

    past = Event.objects.annotate().filter(event_start_time__lt=now).reverse() #tidligere events, reverseres for å få eldste sist
    context = { #pusher til to variabler, hentes inn i all-events.html
        'past_events': past,
        'upcoming_events': upcoming
    }

    return render(request, 'events/all-events.html', context)


def create_event(request):
    # Calls 403 - permission denied if not logged in
    if request.user.is_staff:

        form = CreateEventForm(request.POST or None, request.FILES or None)

        context = {
            'form': form
        }

        if form.is_valid():
            instance = form.save(commit=False)
            # image = form.cleaned_data['image']
            instance.save()
            return redirect('event', event_slug=instance.slug)

        return render(request, 'events/create-event.html', context)
    else:
        raise PermissionDenied


def checkClass(user, event):
    has_access = False

    if user.get_class_year() == 1 and event.class_1:
        has_access = True
    if user.get_class_year() == 2 and event.class_2:
        has_access = True
    if user.get_class_year() == 3 and event.class_3:
        has_access = True
    if user.get_class_year() == 4 and event.class_4:
        has_access = True
    if user.get_class_year() == 5 and event.class_5:
        has_access = True
    if user.get_class_year() > 5 and event.alumni:
        has_access = True
    return has_access


def stringBuilder(event):
    if event.class_1 and event.class_2 and event.class_3 and event.class_4 and event.class_4 and event.class_5 and event.alumni:
        open_for_string = "Alle IPD-studenter og alumni"
    elif event.class_1 and event.class_2 and event.class_3 and event.class_4 and event.class_4 and event.class_5:
        open_for_string = "Alle IPD-studenter"
    elif event.class_3 and event.class_4 and event.class_4 and event.class_5:
        open_for_string = "3. - 5. klasse"
    elif event.class_1 and event.class_2:
        open_for_string = "1. og 2. klasse"
    elif event.class_4 and event.class_5:
        open_for_string = "4. og 5. klasse"
    elif event.class_1:
        open_for_string = "1. klasse"
    elif event.class_2:
        open_for_string = "2. klasse"
    elif event.class_3:
        open_for_string = "3. klasse"
    elif event.class_4:
        open_for_string = "4. klasse"
    elif event.class_5:
        open_for_string = "5. klasse"
    else:
        open_for_string = "Noen"

    return open_for_string


def updateButtonEventButton(user, context):
    if context['event'].available_spots:
        context['spots_left'] = context['event'].available_spots - \
            context['event'].registered_users.count()
    if context['event'].available_spots is not None:
        if context['event'].registered_users.all().count() >= context['event'].available_spots:
            context['buttonText'] = "Legg deg i ventelisten"
            context['buttonState'] = True
    # If user is logged in
    if user.is_authenticated:
        context['loginSuccess'] = True
        # Check if in correct class
        if not checkClass(user, context['event']):
            context['buttonText'] = "Ikke tilgang"
            context['buttonState'] = False
        # If on waitinglist
        elif user in context['event'].registered_users.all():
            context['buttonText'] = "Du er påmeldt"
            context['buttonState'] = False
        # If on waitinglist
        elif user in context['event'].waiting_list.all():
            context['buttonText'] = "Du står på venteliste"
            context['buttonState'] = False
        elif not user.komite is not None and context['event'].only_komite:
            context['buttonText'] = "Bare for komitéer"
            context['buttonState'] = False
        elif context['event'].available_spots:
            if context['event'].registered_users.count() >= context['event'].available_spots:
                context['buttonText'] = 'Fullt'
                context['buttonState'] = False
                context['event_full'] = True
    if context['event'].registration_start_time >= timezone.now():
        context['buttonText'] = "Påmelding ikke åpnet enda"
        context['buttonState'] = False
        context['not_open_yet'] = True

    return context


def event(request, event_slug):
    user = request.user
    # user.update_class_year() # Updates user to alumni if old enough
    event = Event.objects.get(slug=event_slug)
    # Whenever someone enters the event page. Waiting list is updated

    # event.update_waiting_list()
    # Generates a string based on who the event is open for
    open_for_string = stringBuilder(event)

    # On load data
    context = {
        'event': event,
        'user': user,
        'open_for': open_for_string,
        'not_open_yet': False,
        'loginSuccess': False,
        'buttonText': 'Meld deg på',
        'buttonState': True,
        'event_full': False,
        'spots_left': 0
    }

    # HTTP Part
    # GET (On page load)
    if request.method == 'GET':
        context = updateButtonEventButton(user, context)
        return render(request, 'events/event-detail.html', context)

    # POST (User sending data) requests are only necessary if event
    # has registration
    elif request.method == 'POST':
        # If request doesn't contain an email. It is a sign-up request
        if event.registration_required and checkClass(user, event) and (not context['not_open_yet']) and (not context['event_full']) and ((event.only_komite and user.komite is not None) or (not event.only_komite)):
            event.registered_users.add(user)
            context['registerSuccess'] = True
            context = updateButtonEventButton(user, context)
        # Event and Profile are not json serializable so have to be removed before it's sent
        return render(request, 'events/event-detail.html', context)


def event_admin(request, event_slug):
    event = Event.objects.get(slug=event_slug)
    context = {"event": event,
               'registered_users': event.registered_users.order_by('-graduation_year', 'first_name')}

    if (request.user.is_staff):
        return render(request, 'events/event-admin.html', context)
    else:
        raise PermissionDenied


def send_event_confirmation_mail(subject, message, user_email):
    send_mail(
        subject,  # Subject
        message,  # Message
        settings.EMAIL_HOST_USER,  # From email
        [user_email],  # To email
        fail_silently=False,
    )
