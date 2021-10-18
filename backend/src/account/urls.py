from django.urls import path
from . import views

urlpatterns = [
    path("login", views.loginApi, name="login"),
    path("register", views.registerApi, name="register"),
    path("profile", views.profileApi, name="profile"),
    path("staff", views.staffProfile, name="staff"),
]
