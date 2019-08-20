from django.urls import path

from . import views

urlpatterns = [
    path('student/jobb', views.job, name='job'),
    path('student/jobb/<slug:job_slug>', views.job_detail, name='job-detail'),
]
