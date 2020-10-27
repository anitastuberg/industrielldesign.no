from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.utils import timezone

from .models import Komite, Kontaktperson
from .models import TheSign, Nyhet

# Create your views here.


def about(request):
    contacts = Kontaktperson.objects.all().order_by('rank')

    context = {
        'kontaktpersons': contacts
    }
    return render(request, 'leonardo/about.html', context)


def komiteer(request):
    context = {
        'komiteer': Komite.objects.all()
    }
    return render(request, 'leonardo/komite.html', context)


def komite_detail(request, komite_slug):
    context = {
        'komite': Komite.objects.get(slug=komite_slug)
    }
    return render(request, 'leonardo/komite-detail.html', context)


def thesign(request):
    context = {
        'thesigns': TheSign.objects.all()
    }
    return render(request, 'leonardo/thesign.html', context)


def vedtekter(request):
    if request.user.is_authenticated:
        return render(request, 'leonardo/vedtekter.html', {})
    else:
        return HttpResponseForbidden()

def nyheter(request):
    now = timezone.now()
    past = Nyhet.objects.annotate().filter(post_time__lt=now)
    context = {
        'nyheter': past
    }
    return render(request, 'leonardo/nyheter.html', context)

def nyhet(request, nyhet_slug):
    context = {
        'nyhet': Nyhet.objects.get(slug=nyhet_slug)
    }
    return render(request, 'leonardo/nyheter-detail.html', context)
