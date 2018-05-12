from django import forms
from django.core.exceptions import ValidationError


from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'image', 'category']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        return title
    
    # def clean_image(self):
    #     image = self.cleaned_data.get('image', False)
    #     if image:
    #         if image._size > 10*1024*1024:
    #             raise ValidationError("Image file too large ( > 10mb )")
    #         return image
    #     else:
    #         raise ValidationError("Couldn't read uploaded image")