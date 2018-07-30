from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.core.exceptions import ValidationError
from .forms import LoginForm, RegisterForm

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
            allergies = form.cleaned_data['allergies']
            user.set_password(password)
            user.save()

            # Return s User ovbjects if credentials are correct
            user = authenticate(email=email, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user) # Loging in user to the website
                    return redirect('index')

        return  render(request, self.template_name, {'form': form})
