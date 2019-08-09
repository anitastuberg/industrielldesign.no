from django.urls import path

from . import views

urlpatterns = [
    path('min-profil', views.my_profile, name="my_profile"),
    path('api/delete-book', views.delete_book, name="delete_book")
]
