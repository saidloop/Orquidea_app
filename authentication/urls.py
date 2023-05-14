from django.conf import settings
from django.urls import path
from . import views
from .views import RegisterUserView, LoginUserView, LogoutUserView, ListUserView
from django.contrib.auth import views as auth_views


app_name = 'authentication'

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),

    path('user/', ListUserView.as_view(), name='list_user'),
    path('user/register/', RegisterUserView.as_view(), name='register'),

]
