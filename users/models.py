from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class UserProfil(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    imagepersonnaliser = models.ImageField(upload_to='users', blank=True, null=True)
    name = models.CharField( max_length=50)
    fullname = models.CharField( max_length=50)
    email =  models.EmailField()
    telephone = models.IntegerField()
    password = models.CharField(max_length=50)
    statutprofessionnel = models.CharField( max_length=50)
    revenueannuel = models.IntegerField()
    objectiffinanciaire = models.TextField()
    commentaire = models.TextField()
    date_heure = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.user.username