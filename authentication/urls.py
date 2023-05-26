from django.conf import settings
from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_views


app_name = 'authentication'

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),

    path('user/', ListUserView.as_view(), name='list_user'),
    path('user/register/', RegisterUserView.as_view(), name='register'),
    path('user/update/<int:user_id>/', UpdateUserView.as_view(), name='update_user'),
    path('user/deactivate/<int:profile_id>/', DeactivateUserView.as_view(), name='deactivate_user'),
    path('user/deactivate/<int:profile_id>/confirm/', DeactivateUserView.as_view(), name='deactivate_user_confirm'),
    path('user/activate/<int:profile_id>/', ActivateUserView.as_view(), name='activate_user'),
    path('user/activate/<int:profile_id>/confirm/', ActivateUserView.as_view(), name='activate_user_confirm'),

]
