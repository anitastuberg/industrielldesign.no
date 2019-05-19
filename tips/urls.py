from django.urls import path

from . import views

urlpatterns = [
    path('tips/', views.tips, name='tips'),
    path('nytt-tips', views.new_tip, name='new-tip')
]
