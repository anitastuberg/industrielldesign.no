from django.urls import path
from django.conf import settings
from django.contrib.auth.views import logout

from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),
    # Leonardo
    path('leonardo', views.leonardo, name='leonardo'),
    path('leonardo/butikk/', views.leonardo_shop, name='leonardo-shop'),
    path('leonardo/komiteer/', views.Komiteer, name='komiteer'),
    path('leonardo/om/', views.about, name='about'),
    path('leonardo/thesign/', views.thesign, name='thesign'),
    # Student
    path('student/', views.student, name="student"),
    path('student/klassetur/', views.klassetur, name='klassetur'),
    path('student/utveksling/', views.utveksling, name='utveksling'),
    path('student/ny-student/', views.ny_student, name='ny-student'),
    path('404/', views.snake, name='404'),
    path('brukervilkår', views.terms, name='terms'),
]
