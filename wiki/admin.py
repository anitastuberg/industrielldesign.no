from django.contrib import admin


# Register your models here.
from .forms import ArticleForm
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ["__str__", "created", "updated", 'visits', 'editable']
    fields = ('title', 'introduction', 'body_text', 'editable')

    class Meta:
       model = Article

admin.site.register(Article, ArticleAdmin)