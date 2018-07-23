from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    image = ProcessedImageField(upload_to='styremedlem/',processors=[ResizeToFit(2000, 2000, False)], format='JPEG', options={'quality': 85})
    creator = models.ForeignKey(User, editable=False)
    creation_date = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = "Prosjekt"
        verbose_name_plural = "Prosjekter"