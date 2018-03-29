from django import forms

from .models import EventOpen, EventRegister

class CreateEventOpenForm(forms.ModelForm):

    title = forms.CharField(max_length=150)

    class Meta:
        model = EventOpen
        fields = ['title', 'description', 'event_start_time', 'event_start_date']

class CreateEventRegisterForm(forms.ModelForm):

    title = forms.CharField(max_length=150)

    class Meta:
        model = EventRegister
        fields = ['title', 'description', 'event_start_time', 'event_start_date', 'registration_start_date', 'registration_start_time', 'available_spots']