from django.contrib import admin

# Register your models here.
from .forms import CreateEventForm
from .models import Event, EventImage


class EventAdmin(admin.ModelAdmin):
    list_display = ["__str__", "event_start_time"]
    form = CreateEventForm
    filter_horizontal = ('registered_users', 'waiting_list')
    ordering = ('-event_start_time',)
    class Meta:
        model = Event


class EventImageAdmin(admin.ModelAdmin):
    list_display = ['event']

    class Meta:
        model = EventImage


admin.site.register(Event, EventAdmin)
admin.site.register(EventImage, EventImageAdmin)