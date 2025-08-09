from django.urls import path
from .views import *

urlpatterns = [
    path('rapport',rapport, name='rapport'),
]
