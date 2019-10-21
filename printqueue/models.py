from django.db import models


# Create your models here.


class Printer(models.Model):
    name = models.CharField(max_length=100)


class Job(models.Model):
    printer = models.ForeignKey(Printer, on_delete=models.CASCADE)
