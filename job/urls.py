from django.urls import path

from . import views

urlpatterns = [
    path('jobb', views.job, name='job'),
]
