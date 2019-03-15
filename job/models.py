from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=100)
    deadline = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Stillingsannonse'
        verbose_name_plural = 'Stillingsannonser'
