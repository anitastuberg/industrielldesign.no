from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFit, ResizeToFill
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe
import datetime


# Create your models here.
class TheSign(models.Model):

    EDITION_CHOICES = [
        ('1. utgave', '1. utgave'),
        ('2. utgave', '2. utgave'),
        ('3. utgave', '3. utgave'),
        ('4. utgave', '4. utgave'),
    ]

    url = models.CharField(max_length=500)
    edition = models.CharField(max_length=20, choices=EDITION_CHOICES)
    year = models.PositiveIntegerField(choices=[(r, r) for r in range(
        1994, datetime.date.today().year + 1)], default=datetime.date.today().year)
    image = ProcessedImageField(upload_to='komite/', processors=[ResizeToFit(
        500, 500, False)], format='JPEG', options={'quality': 85}, null=True)

    def __str__(self):
        return "%s %s" % (self.edition, self.year)

    class Meta:
        ordering = ['-year', '-edition']


class Komite(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = ProcessedImageField(upload_to='komite/', processors=[ResizeToFit(
        1200, 1200, False)], format='JPEG', options={'quality': 85})
    slug = models.SlugField(max_length=200)

    def save(self, *args, **kwargs):
        if not self.id:
            # Only set the slug when the object is created.
            # Does not update to make sure links doesn't get broken
            self.slug = slugify(self.name)
        super(Komite, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Kontaktperson(models.Model):
    name = models.CharField(max_length=250)
    image = ProcessedImageField(upload_to='komite/', processors=[ResizeToFit(
        500, 500, False)], format='JPEG', options={'quality': 85})
    hoverImage = ProcessedImageField(upload_to='komite/', processors=[ResizeToFit(
        500, 500, False)], format='JPEG', options={'quality': 85}, null=True)
    email = models.CharField(max_length=250)
    stilling = models.CharField(max_length=250)
    rank = models.PositiveSmallIntegerField(default='0')

    def __str__(self):
        return self.name


class Nyhet(models.Model):
    title = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    post_time = models.DateTimeField()
    image = ProcessedImageField(upload_to='nyheter/', processors=[ResizeToFit(2000, 2000, False)], format='JPEG',
                                options={'quality': 85})
    thumbnail = ImageSpecField(source='image', processors=[
        ResizeToFill(300, 300, False)], format='JPEG',
        options={'quality': 100})
    slug = models.SlugField(max_length=60, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Nyhet, self).save(*args,**kwargs)

    class Meta:
        verbose_name = 'Nyhet'
        verbose_name_plural = 'Nyheter'
        ordering = ['-post_time', 'title']