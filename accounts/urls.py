from django.urls import path

from . import views


urlpatterns = [
    path("login/", views.loginUser, name="login"),
    path("register/", views.registerReader, name="register"),
    path("staff-register/", views.registerLibrarian, name="staff-register"),
    path("logout/", views.logoutUser, name="logout"),
]
