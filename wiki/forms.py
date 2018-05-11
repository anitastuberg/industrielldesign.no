from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'image', 'category']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        return title