from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    # Event start
    event_start_time = models.TimeField()
    event_start_date = models.DateField()

    # Event header image:
    # image = models.ImageField()

    def __str__(self):
        return self.title

    class Meta:
        abstract = True

class EventOpen(Event):
    class Meta:
        ordering = ['event_start_date']
        verbose_name = 'Open event'
        verbose_name_plural = 'Open events'

class EventRegister(Event):
    # Registration opens
    registration_start_time = models.TimeField()
    registration_start_date = models.DateField(max_length=500)

    # Available spots in the event
    available_spots = models.IntegerField()

    class Meta:
        ordering = ['event_start_date']
        verbose_name = 'Event with registration'
        verbose_name_plural = 'Events with registration'
        
    

