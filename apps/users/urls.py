from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.conf.urls.static import  static 
from django.conf import settings

urlpatterns =[
    path('accounts/login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("register/", views.register, name="register"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),

    path("view_user/<str:user>/", views.view_user, name="view_user"),
    path('follow/<int:user_id>', views.follow_user, name='follow'),
    path('unfollow/<int:user_id>', views.unfollow_user, name='unfollow')
]