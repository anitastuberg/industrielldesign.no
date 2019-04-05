from django import forms

from .models import Project


class CreateProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateProjectForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['autocomplete'] = "off"
        self.fields['title'].widget.attrs['placeholder'] = "."
        self.fields['description'].widget.attrs['placeholder'] = "."
        self.fields['creator'].widget.attrs['placeholder'] = "."
        self.fields['course'].widget.attrs['placeholder'] = "."

    class Meta:
        model = Project
        fields = ['title', 'description', 'creator', 'course', 'semester', 'year']