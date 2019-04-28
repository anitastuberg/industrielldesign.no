from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

from authentication.models import Profile
from courses.models import Course


class Book(models.Model):
    title = models.CharField(max_length=500)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    price = models.PositiveIntegerField()
    added_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = ProcessedImageField(upload_to='events/',processors=[ResizeToFit(800, 800, False)], format='JPEG', options={'quality': 85})

    def __str__(self):
        return self.title