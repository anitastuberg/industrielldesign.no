from django import forms


class CreateCourseForm(forms.Form):
    name = forms.CharField(max_length=400, widget=forms.TextInput(attrs={
        'autocomplete': 'off',
        'placeholder': '.'
    }))
    course_code = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'autocomplete': 'off',
        'placeholder': '.'
    }))


class CreateCourseReviewForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={
        'autocomplete': 'off',
        'placeholder': '.'
    }))