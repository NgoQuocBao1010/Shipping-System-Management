from django.urls import path
from . import views

urlpatterns = [
    path("login", views.loginApi, name="login"),
    path("register", views.registerApi, name="register"),
    path("verify", views.verifyAccount, name="verifyAccount"),
    path("profile/<str:email>", views.profile, name="profile"),
    path("list", views.profileList, name="profileList"),
]
