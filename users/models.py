from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfil(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    imagepersonnaliser = models.ImageField( upload_to='users', height_field=None, width_field=None, max_length=None)
    name = models.CharField( max_length=50)
    fullname = models.CharField( max_length=50)
    email =  models.EmailField()
    telephone = models.IntegerField(max_length=9)
    password = models.CharField(max_length=50)
    statutprofessionnel = models.CharField( max_length=50)
    ville = models.CharField( max_length=50)
    situationfamiliale = models.CharField( max_length=50)
    revenueannuel = models.IntegerField()
    objectiffinanciaire = models.TextField()
    commentaire = models.TextField()
