from django.urls import path

from . import views

urlpatterns = [
    path('tips/', views.tips, name='tips'),
]
