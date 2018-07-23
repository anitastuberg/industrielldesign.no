from django.contrib import admin

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'creator', 'creation_date']