from django.db import models
from django.contrib.auth.models import User

from category.models import * 
# Create your models here.
class Revenue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categorie = models.ForeignKey(CategoryRevenue, on_delete=models.CASCADE)
    montant = models.IntegerField()
    description = models.TextField()
    daterevenue = models.DateTimeField( auto_now_add=False)
    date = models.DateTimeField(auto_now_add=False)
    datemodification = models.DateField(auto_now_add=False)

class Depense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorydepense, on_delete=models.CASCADE)
    montant = models.IntegerField()
    description = models.TextField()
    datedepense = models.DateTimeField( auto_now_add=False)
    date = models.DateTimeField(auto_now_add=True)
    datemodification = models.DateField(auto_now_add=True)
    
        