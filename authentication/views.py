from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.views.generic import View
from django.core.exceptions import ValidationError
from .forms import LoginForm, RegisterForm
from django.core.mail import send_mail

# Create your views here.
class LoginFormView(View):

    template_name = 'home/login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            user.update_class_year()
            return redirect('students')
    
        # Refreshes the login form if not correct
        return  render(request, self.template_name, {'form': form})
    
        
def send_confiramtion_email(user_email):
    send_mail(
        "Velkommen til Leonardos nettside", # Subject
        "Hei!\nVelkommen til Leonardos nettside. Her kan du melde deg på arrangementer, legge ut prosjektene dine på prosjektsiden og skrive artikler til wikisiden vår.\n\nMvh. Leonardo linjeforening", # Message
        settings.EMAIL_HOST_USER, # From email
        [user_email], # To email
        fail_silently=False,
    )


class RegisterFormView(View):
    form_class = RegisterForm
    template_name = 'home/register.html'

    # display a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            print(form.cleaned_data['email'])
            
            # Cleaned (normalized) data
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            allergies = form.cleaned_data['allergies']
            user.set_password(password)
            user.save()

            # Returns User ovbjects if credentials are correct
            user = authenticate(email=email, password=password)

            if user is not None:
                send_confiramtion_email(user.email)
                if user.is_active:
                    login(request, user) # Loging in user to the website
                    return redirect('students')

        return  render(request, self.template_name, {'form': form})
