from django.urls import path
from . import views

urlpatterns = [
    path("login", views.loginApi, name="login"),
    path("profile", views.profileApi, name="profile"),
]
