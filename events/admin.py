from django.contrib import admin

# Register your models here.
from .forms import CreateEventForm
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ["__str__", "event_start_time"]
    form = CreateEventForm
    class Meta:
        model = Event

admin.site.register(Event, EventAdmin)