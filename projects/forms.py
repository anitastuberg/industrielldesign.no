from django import forms

from .models import Project

class CreateProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['title', 'description', 'creator', 'course', 'semester', 'year', 'thumbnail']

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.size > 20*1024*1024:
                raise ValidationError("Image file too large ( > 20mb )")
            return image
        else:
            raise ValidationError("Couldn't read uploaded image")