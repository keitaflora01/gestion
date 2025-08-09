from django.urls import path
from .import views
from .views import *

urlpatterns = [
    path('objectif', objectif, name= 'objectif'),
    path('inscription', ajouterobjectif, name='ajouterobjectif'), 
    path('objectif/modifier/<int:objectif_id>/',modifierobjectif, name='modifierobjectif'),
    path('objectif/supprimer/<int:objectif_id>/',supprimerobjectif,name='supprimerobjectif'),

]