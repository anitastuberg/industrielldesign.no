from django import forms

from .models import Article

class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split('@')
        domain, extension = provider.split('.')

        if not domain == "usc":
            raise forms.ValidationError('Please make sure you use your USC email')
        if not extension == "edu":
            raise forms.ValidationError('Please use a valid .edu email address')
        return "abc@gmail.com"


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text']

    # Validering av epost
    '''def clean_email(self):
        email = (self.cleaned_data.get('email'))
        email_base, provider = email.split('@')
        domain, extension = provider.split('.')

        if not domain == "USC":
            raise forms.ValidationError('Please make sure you use your USC email')
        if not extension == "edu":
            raise forms.ValidationError("Please use a valid .EDU email address")
        return "abc@gmail.com" '''

    def clean_title(self):
        title = self.cleaned_data.get('title')
        return title