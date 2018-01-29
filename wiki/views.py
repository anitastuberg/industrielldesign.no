from django.shortcuts import render

def wiki(request):
    return render(request, 'wiki/wiki.html')
