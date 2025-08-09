from django.db import models
from django.contrib.auth.models  import User
# Create your models here.

class Rapport(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     name = models.CharField(max_length=50)
     typeraport = models.CharField(max_length=50)
     date = models.DateTimeField( auto_now_add=False)