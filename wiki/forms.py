from django import forms
from django.core.exceptions import ValidationError


from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'image', 'category']

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget = forms.TextInput(attrs={
            'name': 'Tittel',
            'placeholder': 'Tittel...'})
        self.fields['text'].widget = forms.Textarea(attrs={
        'name': 'Brødtekst',
        'class' : 'autoExpand',
        'rows' : '3',
        'data-min-rows' : '3',
        'placeholder': 'Skriv artikkelen her...'})

    def clean_title(self):
        title = self.cleaned_data.get('title')
        return title
    
    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image._size > 20*1024*1024:
                raise ValidationError("Image file too large ( > 20mb )")
            return image
        else:
            raise ValidationError("Couldn't read uploaded image")