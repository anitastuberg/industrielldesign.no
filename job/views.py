import datetime

from django.shortcuts import render

from job.models import Job, JobFilter


def job(request):
    def add_years():
        d = datetime.date.today()
        years = 2
        try:
            return d.replace(year=d.year + years)
        except ValueError:
            return d + (datetime.date(d.year + years, 1, 1) - datetime.date(d.year, 1, 1))
    context = {
        "jobs": Job.objects.filter(deadline__range=(datetime.date.today(), add_years())),
        'filters': JobFilter.objects.all()
    }

    return render(request, 'job/jobb.html', context)


def job_detail(request, job_slug):
    job = Job.objects.get(slug=job_slug)
    context = {
        'job': job
    }
    return render(request, 'job/job-detail.html', context)
