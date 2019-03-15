from django.db import models


class Job(models.Model):
    job_title = models.CharField(max_length=100)
    job_deadline = models.DateTimeField() # Legg inn frist her.
    job_description = models.TextField()

    def __str__(self):
        return self.job_title

    class Meta:
        verbose_name = 'Stillingsannonse'
        verbose_name_plural = 'Stillingsannonser'
