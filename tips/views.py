from django.shortcuts import render


def tips(request):
    return render(request, 'tips/tips.html', {})