from django.urls import path

from . import views

urlpatterns = [
    path('tips/', views.tips, name='tips'),
    path('nytt-tips/', views.new_tip, name='new-tip'),
    path('rediger-tips/<slug:tip_slug>', views.edit_tip, name='edit-tip'),
    path('tips/<slug:tip_slug>', views.tip_page, name='tip-page'),
]
