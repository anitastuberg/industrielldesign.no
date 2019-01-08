from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from django.conf import settings
from django.template.defaultfilters import slugify  
import datetime

# Create your models here.
class ProjectImage(models.Model):
    image = ProcessedImageField(upload_to='projectimages/',processors=[ResizeToFit(2000, 2000, False)], format='JPEG', options={'quality': 85})

class Project(models.Model):

    HØST = 'H'
    VÅR = 'V'
    SEMESTER_CHOICES = (
        (HØST, 'Høst'),
        (VÅR, 'Vår')
    )
    YEAR_CHOICES = [(r,r) for r in range(datetime.datetime.now().year-10, datetime.datetime.now().year+1)]
    

    title = models.CharField(max_length=150, unique=True)
    description = models.TextField()

    creator = models.CharField(max_length=300)
    year = models.IntegerField('År', choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    semester = models.CharField(max_length=2, choices=SEMESTER_CHOICES, default=HØST)
    course = models.CharField(max_length=150, blank=False, null=False)
    
    thumbnail = ProcessedImageField(upload_to='projects/', processors=[ResizeToFit(1500, 1500, False)], format='JPEG', options={'quality': 85})
    
    creation_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    slug = models.SlugField(max_length=60, blank=True)

    def __str__(self):
        return self.title;

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Prosjekt"
        verbose_name_plural = "Prosjekter"