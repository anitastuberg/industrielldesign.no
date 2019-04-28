from django.urls import path

from . import views

urlpatterns = [
    path('boksalg', views.books, name="books"),
    path('legg-ut-bok', views.create_book, name="create-book")
]