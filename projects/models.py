from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from django.conf import settings
from django.template.defaultfilters import slugify  
import datetime


# Create your models here.
class ProjectImage(models.Model):
    image = ProcessedImageField(upload_to='projectimages/',processors=[ResizeToFit(2000, 2000, False)], format='JPEG', options={'quality': 85})
    project = models.ForeignKey('Project', on_delete=models.CASCADE, blank=True, null=True)


class Project(models.Model):

    HØST = 'Høst'
    VÅR = 'Vår'
    YEAR_CHOICES = [
        ('1. klasse', '1. klasse'),
        ('2. klasse', '2. klasse'),
        ('3. klasse', '3. klasse'),
        ('4. klasse', '4. klasse'),
        ('5. klasse', '5. klasse'),
    ]
    

    title = models.CharField(max_length=150, unique=True)
    description = models.TextField()

    creator = models.CharField(max_length=300)
    class_year = models.CharField('Klasse', choices=YEAR_CHOICES, max_length=10)
    course = models.CharField(max_length=150, blank=False, null=False)
    
    creation_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    slug = models.SlugField(max_length=60, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Prosjekt"
        verbose_name_plural = "Prosjekter"
        ordering = ('creation_date', 'title')