from django.contrib import admin

from .models import TheSign, Komite



class TheSignAdmin(admin.ModelAdmin):
    class Meta:
        model = TheSign


class KomiteAdmin(admin.ModelAdmin):
    class Meta:
        model = Komite


admin.site.register(TheSign, TheSignAdmin)
admin.site.register(Komite, KomiteAdmin)