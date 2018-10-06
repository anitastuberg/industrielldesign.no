from django import forms

from .models import Event

class CreateEventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = [
            'title', 
            'description', 
            'location', 
            'image', 
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
            'waiting_list'
        ]

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.size > 20*1024*1024:
                raise ValidationError("Image file too large ( > 20mb )")
            return image
        else:
            raise ValidationError("Couldn't read uploaded image")