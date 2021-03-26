from django.urls import path

from . import views
# from .views import *

urlpatterns = [
    # Home
    path('', views.home, name='home'),

    # Student
    path('student/klassetur/', views.klassetur, name='klassetur'),
    path('student/utveksling/', views.utveksling, name='utveksling'),
    path('student/ny-student/', views.ny_student, name='ny-student'),
    path('vilkår/', views.terms, name='terms'),

    # Printer
    path('student/printer/', views.printer, name='printer'),
    path('student/printer/queues/', views.PrintQueues.as_view(), name='get_job_queues'),
    path('student/printer/job/', views.PrintJobClass.as_view(), name='create_job'),
    path('student/printer/job/<int:pk>/', views.PrintJobClass.as_view(), name='delete_job'),

    
    
]
