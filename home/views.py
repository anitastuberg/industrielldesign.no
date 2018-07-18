from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.core.exceptions import ValidationError
from .forms import LoginForm, RegisterForm
from events.models import Event

def index(request):
    return render(request, 'home/index.html', {})

def about(request):
    return render(request, 'home/about.html', {})

def projects(request):
    return render(request, 'home/projects.html', {})

def students(request):

    context = {
        "events": Event.objects.all()
    }

    return render(request, 'home/students.html', context)

def snake(request):
    return render(request, 'testing/404/404.html', {})

class LoginFormView(View):

    template_name = 'home/login.html'
    form_class = RegisterForm

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
            return redirect('students')
    
        # Refreshes the login form if not correct
        return  render(request, self.template_name, {'form': form})
    
        



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
            
            # Cleaned (normalized) data
            # username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # Return s User ovbjects if credentials are correct
            user = authenticate(email=email, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user) # Loging in user to the website
                    return redirect('index')

        return  render(request, self.template_name, {'form': form})
