from django import forms

from .models import Event

class CreateEventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'image', 'open_for', 'event_start_time', 'event_end_time', 'registration_required', 'registration_start_time', 'available_spots', 'registered_users' ]