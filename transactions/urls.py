from django.urls import path
from .views import *

urlpatterns = [
    path('depensetableau',depensetableau, name="depensetableau"),
    path('revenuetableau',revenuetableau, name="revenuetableau"),
    path('ajouterdepense/',ajouterdepense, name="ajouterdepense"),
    path('ajouterrevenue/', ajouterrevenue, name="ajouterrevenue"),
    path('modifierdepense/<int:depense_id>/modifier/',modifierdepense, name='modifierdepense'),
    path('detaildepense/<int:depense_id>/',detaildepense, name='detaildepense'),
    path('supprimerdepense/<int:depense_id>/supprimer/',supprimerdepense, name='supprimerdepense'),
    path('modifierrevenue/<int:revenue_id>/modifier/',modifierrevenue, name='modifierrevenue'),
    path('detailrevenue/<int:revenue_id>/',detailrevenue, name='detailrevenue'),
    path('supprimerrevenue/<int:revenue_id>/supprimer/',supprimerrevenue, name='supprimerrevenue'),
    path('recherchedepense/<int:depense_id>/',recherchedepense,name='recherchedepense'),

]
