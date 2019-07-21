from django.urls import path

from . import views

urlpatterns = [
    path('student/tips/', views.tips, name='tips'),
    path('student/nytt-tips/', views.new_tip, name='new-tip'),
    path('student/rediger-tips/<slug:tip_slug>', views.edit_tip, name='edit-tip'),
    path('student/tips/<slug:tip_slug>', views.tip_page, name='tip-page'),
]
