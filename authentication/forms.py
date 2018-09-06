from django.contrib.auth import get_user_model
from django import forms
from .validators import validate_stud_email

User = get_user_model()

class RegisterForm(forms.ModelForm):
    email = forms.EmailField(validators=[validate_stud_email])
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    graduation_year = forms.IntegerField()
    allergies = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['autocomplete'] = "email"
        self.fields['first_name'].widget.attrs['autocomplete'] = "given-name"
        self.fields['last_name'].widget.attrs['autocomplete'] = "family-name"
        self.fields['last_name'].widget.attrs['autocomplete'] = "family-name"
        self.fields['password'].widget.attrs['autocomplete'] = "current-password"


    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'graduation_year', 'allergies', 'password']

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)