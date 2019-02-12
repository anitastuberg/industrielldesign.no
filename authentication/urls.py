from django.urls import path
from django.conf import settings
from django.contrib.auth.views import logout

from django.contrib.auth.views import (password_reset, password_reset_done, password_reset_confirm,
                                       password_reset_complete
                                       )

from . import views

urlpatterns = [
    path('register/', views.RegisterFormView.as_view(), name='register'),
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('reset-password/', password_reset, name="reset_password"),
    path('reset-password/done', password_reset_done, name="password_reset_done"),
    path('reset-password/confirm/(?P<uidb64>[\w-]+)/(?P<token>[\w-]+', password_reset_confirm, name="password_reset_confirm"),
    path('reset-password/complete', password_reset_complete, name="password_reset_complete")
]