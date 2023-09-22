from django.urls import path

from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('leonardo/nyheter/', views.nyheter, name='nyheter'),
    path('leonardo/nyheter/<slug:nyhet_slug>', views.nyhet, name='nyhet'),
    path('leonardo/komiteer/', views.komiteer, name='komiteer'),
    path('leonardo/komiteer/<slug:komite_slug>',
         views.komite_detail, name='komite_detail'),
    path('leonardo/om-leonardo/', views.about, name='about'),
    path('leonardo/vedtekter/', views.vedtekter, name='vedtekter'),
    path('leonardo/thesign/', views.thesign, name='thesign'),
    path('leonardo/utleie/', views.utleie, name='utleie'),
    path('leonardo/linktree/', views.linktree, name='linktree'),
    path('leonardo/prikksystem/', views.prikksystem, name='prikksystem'),

    path('folketinget', TemplateView.as_view(template_name="leonardo/folketinget.html"), name="folketinget")
]
