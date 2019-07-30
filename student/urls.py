from django.urls import path

from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),

    # Student
    path('student/klassetur/', views.klassetur, name='klassetur'),
    path('student/utveksling/', views.utveksling, name='utveksling'),
    path('student/ny-student/', views.ny_student, name='ny-student'),
    path('vilkår/', views.terms, name='terms'),
]
