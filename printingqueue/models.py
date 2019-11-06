from django.db import models

from authentication.models import Profile

# Create your models here.
class Printer(models.Model):
	name = models.CharField(max_length=100)
	active = models.BooleanField()

	def __str__(self):
		return self.name

class Printjob(models.Model):
	description = models.TextField()
	duration = models.PositiveIntegerField()
	start_time = models.DateTimeField()
	printer = models.ForeignKey("printer", on_delete=models.CASCADE)
	user = models.ForeignKey(Profile, on_delete=models.CASCADE)
	gcode = models.FileField(blank = True);

	def __str__(self):
		return "Printerjobb: " + self.user.first_name + " " + self.user.last_name