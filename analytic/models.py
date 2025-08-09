from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Objectif(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    titre = models.CharField(max_length=50)
    CATEGORIE_CHOICES = (
        ('Epargnes', 'Epargnes'),
        ('Depenses','Depenses'), 
        ('Dette','Dette'),
        
    )
    categorie = models.CharField(max_length=50, choices=CATEGORIE_CHOICES,default='')
    montantcible = models.IntegerField()
    montantactuel = models.IntegerField()
    datelimite = models.DateField( auto_now_add=False)
    datemodification = models.DateTimeField( auto_now=True)
    date = models.DateField( auto_now=True)
    description = models.TextField()
    
    

# class Budget(models.Model):
#     user = models.ForeignKey(User ,on_delete=models.CASCADE)
#     categorie = models.CharField(max_length=50)
#     montantprevu = models.DecimalField(default= 0, max_digits=10, decimal_places=2)
#     montantdepense = models.DecimalField(default= 0, max_digits=10, decimal_places=2)
#     priorite = models.TextField()
#     commentaire = models.TextField()

# def pourcentage_complete(self):

#     if self.montant_cible == 0:
#         return 0
#     return min(100, int((self.montant_actuel / self.montant_cible) * 100))
class ObjectifComplete(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titre = models.CharField(max_length=100)
    categorie = models.CharField(max_length=50)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_achievement = models.DateTimeField()
    
    def __str__(self):
        return f"{self.titre} (Complété le {self.date_achievement.strftime('%d/%m/%Y')})"
        
    class Meta:
        verbose_name = "Objectif complété"
        verbose_name_plural = "Objectifs complétés"
        ordering = ['-date_achievement']         

