from django.urls import path
from .views import connexion,inscription 

urlpatterns = [
    path('connexion', connexion, name= 'connexion'),
    path('inscription',inscription, name='inscription'),

]