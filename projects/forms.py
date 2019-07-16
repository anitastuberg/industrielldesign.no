from django import forms

from .models import Project


class CreateProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateProjectForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['autocomplete'] = "off"
        self.fields['title'].widget.attrs['placeholder'] = "Tittel"
        self.fields['description'].widget.attrs['placeholder'] = "Beskrivelse"
        self.fields['creator'].widget.attrs['placeholder'] = "Hvem har laget det?"
        self.fields['course'].widget.attrs['placeholder'] = "Fag"

    class Meta:
        model = Project
        fields = ['title', 'description', 'creator', 'course', 'class_year']