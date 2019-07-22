from django.shortcuts import render

from .models import Komite
from .models import TheSign

# Create your views here.
def about(request):
    return render(request, 'leonardo/about.html', {})

def komiteer(request):
    context = {
        'komiteer': Komite.objects.all()
    }
    return render(request, 'leonardo/komite.html', context)

def komite_detail(request, komite_slug):
    context = {
        'komite': Komite.objects.filter(komite_slug=komite_slug)
    }
    return render(request, 'leonardo/komite-detail.html', context)

def thesign(request):
    context = {
        'thesigns': TheSign.objects.all()
    }
    return render(request, 'leonardo/thesign.html', context)

