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

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'graduation_year', 'allergies', 'password']

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)