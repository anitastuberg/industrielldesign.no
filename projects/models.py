from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from django.conf import settings
from django.template.defaultfilters import slugify  
import datetime


# Create your models here.
class ProjectImage(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    image = ProcessedImageField(upload_to='projectimages/',processors=[ResizeToFit(2000, 2000, False)], format='JPEG', options={'quality': 85})
    project = models.ForeignKey('Project', on_delete=models.CASCADE, blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        if not self.project:
            return str(self.pk)
        else:
            return "Bilde til prosjekt nummer: %d" % self.project.pk
    
    class Meta:
        verbose_name = "Prosjektbilde"
        verbose_name_plural = "Prosjektbilder"
        ordering = ('creation_date',)


class Project(models.Model):

    YEAR_CHOICES = [
        ('1. klasse', '1. klasse'),
        ('2. klasse', '2. klasse'),
        ('3. klasse', '3. klasse'),
        ('4. klasse', '4. klasse'),
        ('5. klasse', '5. klasse'),
    ]
    

    description = models.TextField(blank=True, null=True)

    creator = models.CharField(max_length=300, blank=True, null=True)
    class_year = models.CharField('Klasse', choices=YEAR_CHOICES, max_length=10, blank=True, null=True)
    course = models.CharField(max_length=150, blank=True, null=True)
    
    creation_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        if self.creator and self.course:
            return "%s" % (self.creator)
        else:
            return str(self.pk)

    class Meta:
        verbose_name = "Prosjekt"
        verbose_name_plural = "Prosjekter"
        ordering = ('creation_date',)