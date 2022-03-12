from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.conf.urls.static import  static 
from django.conf import settings

urlpatterns =[
    path("", views.home, name="home"),
    path('accounts/login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("register/", views.register, name="register"),
    path("view_user/<str:profile>/", views.view_user, name="view_user"),
]