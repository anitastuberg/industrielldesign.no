from django.db import models
from django.conf import settings

class Event(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()

    location = models.CharField(max_length=50, blank=True, null=True)
    open_for = models.CharField(max_length=50, blank=True, null=True)
    # image = models.ImageField(max_length=100)
    

    # Event start
    event_start_time = models.DateTimeField()
    event_end_time = models.DateTimeField(blank=True, null=True)

    # Registration opens
    registration_start_time = models.DateTimeField(blank=True, null=True)

    # Available spots in the event
    registration_required = models.BooleanField(default=False)
    available_spots = models.IntegerField(blank=True, null=True)
    

    registered_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    # Event header image:
    # image = models.ImageField()

    def __str__(self):
        return self.title

    class Meta:
        # ordering = ['event_start_date']
        verbose_name = 'Event'
        verbose_name_plural = 'Events'