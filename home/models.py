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
    komite = models.CharField(max_length=100)
    post_title = models.CharField(max_length=100)
    post_description = models.TextField()
    post_image = ProcessedImageField(upload_to='styremedlem/',processors=[ResizeToFit(2000, 2000, False)], format='JPEG', options={'quality': 85})

    def __str__(self):
        return self.komite

    class Meta:
        verbose_name = 'Komité'
        verbose_name_plural = 'Komiteer'

class Nyhet(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Nyhet"
        verbose_name_plural = "Nyheter"

# Andy:
class Jobb(models.Model):
    job_title = models.CharField(max_length=100)
    job_deadline = models.DateTimeField() # Legg inn frist her.
    job_description = models.TextField()

    def __str__(self):
        return self.job_title

    class Meta:
        verbose_name = 'Stillingsannonse'
        verbose_name_plural = 'Stillingsannonser'
