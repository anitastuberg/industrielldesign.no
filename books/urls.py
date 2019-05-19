from django.urls import path

from . import views

urlpatterns = [
    path('student/boksalg', views.books, name="books"),
    path('student/boksalg/legg-ut-bok', views.create_book, name="create-book")
]