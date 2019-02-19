from django.contrib import admin

from .models import Styremedlem, Komiteer, Nyhet, Jobb

# Register your models here.
class StyrmedlemAdmin(admin.ModelAdmin):
    list_display = ["__str__", "full_name", "e_mail", "phone_number"]

    class Meta:
        model = Styremedlem

class KomiteerAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    
    class Meta:
        model = Komiteer

class NyheterAdmin(admin.ModelAdmin):
    list_display = ["__str__", "timestamp", "updated"]
    
    class Meta:
        model = Nyhet

# Andy:
class JobbAdmin(admin.ModelAdmin):
    list_display = ["__str__", "job_title", "job_deadline", "job_description"]

    class Meta:
        model = Jobb

admin.site.register(Styremedlem, StyrmedlemAdmin)
admin.site.register(Komiteer, KomiteerAdmin)
admin.site.register(Nyhet, NyheterAdmin)
# Andy:
admin.site.register(Jobb, JobbAdmin)
