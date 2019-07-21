from django import forms

from .models import Event


class CreateEventForm(forms.ModelForm):
    event_start_time = forms.DateTimeField()

    def __init__(self, *args, **kwargs):
        super(CreateEventForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['autocomplete'] = "off"
        self.fields['title'].widget.attrs['placeholder'] = "Tittel"
        self.fields['short_description'].widget.attrs['autocomplete'] = "off"
        self.fields['short_description'].widget.attrs['placeholder'] = "Kort beskrivelse"
        self.fields['description'].widget.attrs['placeholder'] = "Lengre beskrivelse"
        self.fields['location'].widget.attrs['placeholder'] = "Sted"
        self.fields['event_start_time'].widget.attrs['placeholder'] = "Når begynner arrangementet?"
        self.fields['event_end_time'].widget.attrs.update({'type': 'datetime-local'})


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