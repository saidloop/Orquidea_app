from django.conf import settings
from django.urls import path
from . import views
from .views import *

app_name = 'contracts'

urlpatterns = [
    path('contracts/', ListContracts.as_view(), name='list_contracts'),
    path('contracts/register_contract/', RegisterContractView.as_view(), name='register_contract'),
]