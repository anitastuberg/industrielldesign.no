from django.urls import path

from courses import views

urlpatterns = [
    path('student/fag', views.courses, name="courses"),
    path('student/opprett-fag', views.create_course, name="create_course"),
    path('student/fag/<slug:course_slug>', views.course_detail, name='course_detail')
]