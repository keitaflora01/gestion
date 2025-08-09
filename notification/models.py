from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Rappel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField( max_length=50)
    message = models.TextField()
    date = models.DateTimeField( auto_now_add=False)

class Alerte(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objet = models.CharField(max_length=50) 
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=False)


