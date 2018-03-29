from django import forms

from .models import Event

class CreateEventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['title', 'description', 'event_start_time', 'event_start_date', 'registration_start_date', 'registration_start_time','registration_required', 'available_spots']