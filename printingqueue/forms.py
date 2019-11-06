from django import forms

from .models import Printjob

class CreatePrintJob(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreatePrintJob, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['placeholder'] = "Beskrivelse"
        self.fields['duration'].widget.attrs['placeholder'] = "Tid på jobb"
        self.fields['printer'].widget.attrs['placeholder'] = "Printer"
        self.fields['start_time'].widget.attrs['placeholder'] = "Dato"
        self.fields['start_time'].widget.attrs['type'] = "datetime-local"

    class Meta:
        model = Printjob
        fields = ['description', 'duration', 'printer', 'start_time']