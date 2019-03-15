from django.shortcuts import render

from job.models import Job


def job(request):
    context = {
        'Stillingsannonser': Job.objects.all()
    }
    return render(request, 'job/jobb.html', context)