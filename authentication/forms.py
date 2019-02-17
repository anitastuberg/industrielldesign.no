from django.contrib.auth import get_user_model
from django import forms
from .validators import validate_stud_email
import datetime

User = get_user_model()


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['autocomplete'] = "email"
        self.fields['email'].widget.attrs['placeholder'] = "."
        self.fields['first_name'].widget.attrs['autocomplete'] = "given-name"
        self.fields['first_name'].widget.attrs['placeholder'] = "."
        self.fields['last_name'].widget.attrs['autocomplete'] = "family-name"
        self.fields['last_name'].widget.attrs['placeholder'] = "."
        self.fields['allergies'].widget.attrs['autocomplete'] = "off"
        self.fields['allergies'].widget.attrs['placeholder'] = "."
        self.fields['password'].widget.attrs['autocomplete'] = "current-password"
        self.fields['password'].widget.attrs['placeholder'] = "."
        self.fields['graduation_year'].choices = [("", ""),] + list(self.fields["graduation_year"].choices)[1:]
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'graduation_year', 'allergies', 'password', 'is_komite']
        widgets = {
            'password': forms.PasswordInput(),
        }


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)