from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

class Event(models.Model):
    title = models.CharField(max_length=80, unique=True)
    description = models.TextField()

    location = models.CharField(max_length=50, blank=True, null=True)
    open_for = models.CharField(max_length=50, blank=True, null=True)
    image = ProcessedImageField(upload_to='wiki/',processors=[ResizeToFit(2000, 2000, False)], format='JPEG', options={'quality': 85})
    

    # Event start
    event_start_time = models.DateTimeField()
    event_end_time = models.DateTimeField(blank=True, null=True)

    # Registration opens
    registration_start_time = models.DateTimeField(blank=True, null=True)

    # Available spots in the event
    registration_required = models.BooleanField(default=False)
    available_spots = models.IntegerField(blank=True, null=True)
    

    registered_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    
    slug = models.SlugField(max_length=60, blank=True)

    # Event header image:
    # image = models.ImageField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            #Only set the slug when the object is created.
            self.slug = slugify(self.title) #Or whatever you want the slug to use
        super(Event, self).save(*args, **kwargs)

    class Meta:
        # ordering = ['event_start_date']
        verbose_name = 'Event'
        verbose_name_plural = 'Events'