from django.shortcuts import render

def wiki(request):
    render(request, 'wiki/wiki.html')
