from django import forms

from .models import Event


class CreateEventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = [
            'title',
            'short_description',
            'description', 
            'location',
            'event_start_time', 
            'event_end_time', 
            'registration_required', 
            'only_komite',
            'alumni',
            'class_1', 
            'class_2',
            'class_2',
            'class_3',
            'class_4',
            'class_5',
            'registration_start_time',
            'available_spots',
            'registered_users',
            'waiting_list',
            'image'
        ]