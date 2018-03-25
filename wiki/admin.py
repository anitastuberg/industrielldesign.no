from django.contrib import admin


# Register your models here.
from .forms import ArticleForm
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ["__str__", "timestamp", "updated"]
    form = ArticleForm
    #class Meta:
     #   model = Article

admin.site.register(Article, ArticleAdmin)