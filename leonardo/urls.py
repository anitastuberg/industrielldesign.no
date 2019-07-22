from django.urls import path

from . import views

urlpatterns = [
    path('leonardo/komiteer/', views.komiteer, name='komiteer'),
    path('leonardo/komiteer/<slug:komite_slug>', views.komite_detail, name='komite_detail'),
    path('leonardo/om-leonardo/', views.about, name='about'),
    path('leonardo/thesign/', views.thesign, name='thesign'),
]