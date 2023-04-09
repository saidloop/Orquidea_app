from django.conf import settings
from django.urls import path
from . import views
from .views import RegisterUserView, LoginUserView
from django.contrib.auth import views as auth_views


app_name = 'authentication'

urlpatterns = [
    path('register/user', RegisterUserView.as_view(), name='register_user'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', auth_views.logout_then_login, name='logout'),
]
