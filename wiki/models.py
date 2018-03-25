from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    #image = models.ImageField()

    def __str__(self):
        return self.title