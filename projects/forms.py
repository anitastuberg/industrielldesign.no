from django import forms

from .models import Project


class CreateProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateProjectForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['placeholder'] = "Beskrivelse"
        self.fields['creator'].widget.attrs['placeholder'] = "Hvem har laget det?"
        self.fields['course'].widget.attrs['placeholder'] = "Fag"

    class Meta:
        model = Project
        fields = ['description', 'creator', 'course', 'class_year']