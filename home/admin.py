from django.contrib import admin

from .models import Styremedlem, Komiteer, TheSign

# Register your models here.
class StyrmedlemAdmin(admin.ModelAdmin):
    list_display = ["__str__", "full_name", "e_mail", "phone_number"]

    class Meta:
        model = Styremedlem

class KomiteerAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    
    class Meta:
        model = Komiteer


class TheSignAdmin(admin.ModelAdmin):
    list_display = ["__str__"]

    class Meta:
        model = TheSign


admin.site.register(Styremedlem, StyrmedlemAdmin)
admin.site.register(Komiteer, KomiteerAdmin)
admin.site.register(TheSign, TheSignAdmin)
