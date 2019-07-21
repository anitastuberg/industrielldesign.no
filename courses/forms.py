from django import forms


class CreateCourseForm(forms.Form):
    YEAR_CHOICES = [
        ('1.klasse', '1.klasse'),
        ('2.klasse', '2.klasse'),
        ('3.klasse', '3.klasse'),
        ('4.klasse', '4.klasse'),
        ('5.klasse', '5.klasse'),
        ('Ikke trinnavhengig', 'Ikke trinnavhengig')
    ]

    name = forms.CharField(max_length=400, widget=forms.TextInput(attrs={
        'autocomplete': 'off',
        'placeholder': 'Navn'
    }))
    course_code = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'autocomplete': 'off',
        'placeholder': '.',
        'style': 'text-transform: uppercase'
    }))
    class_year = forms.ChoiceField(choices=YEAR_CHOICES)


class CreateCourseReviewForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={
        'autocomplete': 'off',
        'placeholder': 'Skriv noe om faget...'
    }))