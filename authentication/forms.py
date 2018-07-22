from django.contrib.auth import get_user_model
from django import forms
from .validators import validate_stud_email

User = get_user_model()

class RegisterForm(forms.ModelForm):
    email = forms.EmailField(validators=[validate_stud_email])
    password = forms.CharField(widget=forms.PasswordInput)
    allergies = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ['email', 'password', 'allergies']

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)