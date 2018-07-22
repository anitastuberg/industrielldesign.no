from django.urls import path

from . import views

urlpatterns = [
    path('', views.wiki, name="wiki"),
    path('new-article', views.new_article, name="new-article"),
    path('<slug:article>', views.article, name="article")
]