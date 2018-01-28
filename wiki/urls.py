from django.urls import path

from . import views

urlpatterns = [
    path('', views.wiki, name='wiki')
]