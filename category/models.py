from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CategoryRevenue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField( max_length=50, null=False, blank=False) 
    description = models.TextField(default='')
    def __str__(self):
        return self.name


class Categorydepense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField( max_length=50, null=False, blank=False) 
    description = models.TextField(default='')

    def __str__(self):
        return self.name


