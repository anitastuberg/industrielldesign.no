from django.shortcuts import render


def tips(request):
    return render(request, 'tips/tips.html', {})


def new_tip(request):
    return render(request, 'tips/new-tip.html', {})