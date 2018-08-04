from django.urls import path

from . import views

urlpatterns = [
    path('', views.wiki, name="wiki"),
    path('new-article', views.new_article, name="new-article"),
    path('<slug:article_slug>', views.article, name="article"),
    path('edit/<slug:article_slug>', views.edit_article, name="edit-article")
]