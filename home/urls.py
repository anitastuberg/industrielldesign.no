from django.urls import path
from django.conf import settings
from django.contrib.auth.views import logout

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('', views.students, name='students'),
    path('students/komiteer/', views.Komiteer, name='komiteer'),
    path('404/', views.snake, name='404'),
    path('jobb', views.jobb, name='jobb'),
    path('brukervilkår', views.terms, name='terms'),
]
