from django.urls import path
from . import views

urlpatterns = [
    # account authorization
    path("login", views.loginApi, name="login"),
    path("register", views.registerApi, name="register"),
    path("verify/", views.verifyAccount, name="verifyAccount"),
    # profile information
    path("profile/<str:email>", views.profile, name="profile"),
    path("list/", views.profileList, name="profileList"),
    # driver administrator
    path("driver/add", views.createDriver, name="createDriver"),
]
