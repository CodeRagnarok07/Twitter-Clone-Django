from django.urls import path
from . import views

urlpatterns =[
    path("", views.home, name="home"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("view_user", views.view_user, name="view_user"),
]