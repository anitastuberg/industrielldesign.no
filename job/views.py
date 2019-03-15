import datetime

from django.shortcuts import render

from job.models import Job


def job(request):
    def add_years():
        d = datetime.date.today()
        years = 2
        try:
            return d.replace(year=d.year + years)
        except ValueError:
            return d + (datetime.date(d.year + years, 1, 1) - datetime.date(d.year, 1, 1))
    context = {
        "jobs": Job.objects.filter(deadline__range=(datetime.date.today(), add_years()))
    }

    return render(request, 'job/jobb.html', context)