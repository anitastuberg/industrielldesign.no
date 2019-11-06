from django.shortcuts import render

from .models import Printjob
from authentication.models import Profile
from .forms import CreatePrintJob

def printer(request):
	context = {
		"printjobs": Printjob.objects.all,
		"form": CreatePrintJob
	}
	if request.method == "GET":
		return render(request, "printingqueue/3d-printer.html", context)
	else: # POST request
		form = CreatePrintJob(request.POST)
		if form.is_valid and request.user.is_authenticated:
			printjob = form.save(commit=False)
			printjob.user = Profile.objects.get(pk=request.user.pk)
			printjob.save()
		return render(request, "printingqueue/3d-printer.html", context)

