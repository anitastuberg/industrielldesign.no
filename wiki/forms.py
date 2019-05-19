from django import forms
from django.core.exceptions import ValidationError


from .models import Article


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'introduction', 'body_text']
    
    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = "Title..."
        self.fields['title'].widget.attrs['autocomplete'] = "off"
        self.fields['title'].widget.attrs['onkeypress'] = "return event.keyCode!=13"

        self.fields['introduction'].widget.attrs['placeholder'] = "Ingress..."
        self.fields['introduction'].widget.attrs['class'] = "autoResize"
        self.fields['introduction'].widget.attrs['rows'] = "3"

        self.fields['body_text'].widget.attrs['placeholder'] = "Brødtekst..."
        self.fields['body_text'].widget.attrs['class'] = "autoResize"
        self.fields['introduction'].widget.attrs['rows'] = "4"