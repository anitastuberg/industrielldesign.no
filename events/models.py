from django.db import models
from django.conf import settings

class Event(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    # Event start
    event_start_time = models.TimeField()
    event_start_date = models.DateField()

    # Registration opens
    registration_start_time = models.TimeField(blank=True, null=True)
    registration_start_date = models.DateField(max_length=500, blank=True, null=True)

    # Available spots in the event
    registration_required = models.BooleanField(default=False)
    available_spots = models.IntegerField(blank=True, null=True)

    registered_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    # Event header image:
    # image = models.ImageField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['event_start_date']
        verbose_name = 'Event'
        verbose_name_plural = 'Events'