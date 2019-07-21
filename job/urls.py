from django.urls import path

from . import views

urlpatterns = [
    path('student/jobb', views.job, name='job'),
]
