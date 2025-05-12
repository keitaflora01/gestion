from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Analytic(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    montantcible = models.IntegerField()
    montantactuel = models.IntegerField()
    datelimite = models.DateField( auto_now_add=False)
    priorite = models.TextField()



