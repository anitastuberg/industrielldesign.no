from django.shortcuts import render
from django.http import HttpResponseForbidden

from .models import Komite, Kontaktperson
from .models import TheSign

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
