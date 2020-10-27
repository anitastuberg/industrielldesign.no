from django.contrib import admin

from .models import TheSign, Komite, Kontaktperson, Nyhet



class TheSignAdmin(admin.ModelAdmin):
    class Meta:
        model = TheSign


class KomiteAdmin(admin.ModelAdmin):
    class Meta:
        model = Komite

class NyheterAdmin(admin.ModelAdmin):
    list_display = ["__str__", "post_time"]
    ordering = ('-post_time',)
    class Meta:
        model = Nyhet

admin.site.register(TheSign, TheSignAdmin)
admin.site.register(Komite, KomiteAdmin)
admin.site.register(Kontaktperson)
admin.site.register(Nyhet, NyheterAdmin)