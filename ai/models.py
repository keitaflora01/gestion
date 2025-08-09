from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ai(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField( auto_now_add=False)
    context = models.TextField()
