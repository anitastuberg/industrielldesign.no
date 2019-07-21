import datetime

from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


# Create your models here.
class Styremedlem(models.Model):
    styretittel = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200)
    e_mail = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=11)
    profile_picture = ProcessedImageField(upload_to='styremedlem/',
                                          processors=[ResizeToFit(500, 500, False)],
                                          format='JPEG',
                                          options={'quality': 85})

    def __str__(self):
        return self.styretittel

    class Meta:
        verbose_name = 'Styremedlem'
        verbose_name_plural = 'Styremedlemmer'

    
class Komiteer(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = ProcessedImageField(processors=[ResizeToFit(2000, 2000, False)], format='JPEG', options={'quality': 85})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Komité'
        verbose_name_plural = 'Komiteer'


class TheSign(models.Model):
    YEAR_CHOICES = [(r, r) for r in range(datetime.datetime.now().year-10, datetime.datetime.now().year+1)]
    EDITION_NUMBER = [(1, 1), (2, 2), (3, 3), (4, 4)]

    edition_number = models.PositiveSmallIntegerField(choices=EDITION_NUMBER)
    year = models.PositiveIntegerField(choices=YEAR_CHOICES)
    url = models.CharField(max_length=1000)
    cover = ProcessedImageField(upload_to='events/', processors=[ResizeToFit(800, 800, False)], format='JPEG',
                                options={'quality': 85})

    def __str__(self):
        return 'Utgave ' + str(self.edition_number) + ' ' + str(self.year)