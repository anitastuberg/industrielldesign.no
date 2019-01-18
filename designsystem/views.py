from django.shortcuts import render


def design_system(request):
    return render(request, 'designsystem/designsystem.html')
