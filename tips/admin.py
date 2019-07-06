from django.contrib import admin

from tips.models import Tip, Tag


class TipAdmin(admin.ModelAdmin):
    class Meta:
        model = Tip


class TagAdmin(admin.ModelAdmin):
    class Meta:
        model = Tag


admin.site.register(Tip, TipAdmin)
admin.site.register(Tag, TagAdmin)
