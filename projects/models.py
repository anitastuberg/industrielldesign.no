from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    


