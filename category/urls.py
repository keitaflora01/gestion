from django.urls import path
from .views import *

urlpatterns = [
    path('categoriedepense', categoriedepense, name= 'categoriedepense'),
    path('categorierevenue', categorierevenue, name='categorierevenue'),
    path('ajoutercategorieDepense', ajouterCategorieDepense, name='ajoutercategorieDepense'),
    path('ajoutercategorieRevenue', ajouterCategorieRevenue, name='ajoutercategorieRevenue'),
    path('modifierDepense/<int:categorie_id>/', modifiercategoriedepense, name='modifiercategorieDepense'),
    path('modifierRevenue/<int:categorie_id>/', modifiercategorieRevenue, name='modifiercategorieRevenue'),
    path('supprimerDepense/<int:categorie_id>/', supprimercategoriedepense, name='supprimercategorieDepense'),
    path('supprimerRevenue/<int:categorie_id>/', supprimercategorierevenue, name='supprimercategorieRevenue'),

]