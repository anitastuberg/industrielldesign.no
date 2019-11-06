from django.urls import path

from . import views

urlpatterns = [
	path('3d-printer', views.printer, name="3d_printer"),
	path('gcode-reservation', views.printer, name="gcode_reservation")
]