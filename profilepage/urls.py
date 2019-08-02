from django.urls import path

from . import views

urlpatterns = [
    path('min-profil', views.my_profile, name="my_profile"),
    path('min-profil/endre-passord', views.change_password, name="change_password"),
    path('min-profil/endre-info', views.change_info, name="change_info"),
    path('api/delete-book', views.delete_book, name="delete_book")
]
