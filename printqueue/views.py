from django.shortcuts import render

# Create your views here.

from .models import Printer


def printing(request):
    context = {
        'printers': Printer.objects.all
    }
    return render(request, 'printqueue/3d-print-queue.html', context)
