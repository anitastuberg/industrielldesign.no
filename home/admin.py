from django.contrib import admin

from .models import Styremedlem, Komiteer, Nyhet

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

admin.site.register(Styremedlem, StyrmedlemAdmin)
admin.site.register(Komiteer, KomiteerAdmin)
admin.site.register(Nyhet, NyheterAdmin)