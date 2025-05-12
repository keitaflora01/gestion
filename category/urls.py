from django.urls import path
from .views import categorie 

urlpatterns = [
    path('categorie', categorie, name= 'categorie'),

]