from django.contrib import admin

# Register your models here.
from .forms import CreateEventOpenForm, CreateEventRegisterForm
from .models import EventOpen, EventRegister

class EventAdmin(admin.ModelAdmin):
    list_display = ["__str__", "event_start_date", "event_start_time"]
    form = CreateEventOpenForm
    #class Meta:
     #   model = Article

class EventRegisterAdmin(admin.ModelAdmin):
    list_display = ["__str__", "event_start_date", "registration_start_date", "available_spots"]
    form = CreateEventRegisterForm

admin.site.register(EventOpen, EventAdmin)
admin.site.register(EventRegister, EventRegisterAdmin)