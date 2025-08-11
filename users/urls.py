from django.urls import path
from .views import *

urlpatterns = [
    path('connexion', connexion, name= 'connexion'),
    path('inscription',inscription, name='inscription'),
    path('deconnexion/',deconnexion, name='deconnexion'),
    path('profil/',profil_utilisateur, name='profil_utilisateur'),
    path('utilisateurs/', utilisateurs, name='utilisateurs'),
    path('allfeedback/', allfeedback, name='allfeedback'),
]
