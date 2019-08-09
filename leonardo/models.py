from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from django.template.defaultfilters import slugify
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
