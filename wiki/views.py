from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import ArticleForm, ContactForm

def wiki(request):
    title = "Welcome"

    #add a form
    form = ArticleForm(request.POST or None)

    context = {
        "title": title,
        'form': form
    }


    if form.is_valid():
        # form.save()
        instance = form.save(commit=False)

        instance.save()
        context = {
            "title": "Thank you"
        }

    

    return render(request, 'wiki/wiki.html', context)

def contact(request):

    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get('message')
        form_full_name = form.cleaned_data.get('full_name')
        subject = "Site contact form"
        from_email = settings.EMAIL_HOST_USER
        to_email = [settings.EMAIL_HOST_USER, "tobias.wulvik@gmail.com"]
        contact_message = """
        %s: %s via %s
        """%(form_full_name, form_message, form_email)
        send_mail(subject, contact_message, from_email, to_email, fail_silently=False)

    context = {
        "form": form,
    }
    return render(request, 'wiki/forms.html', context)
