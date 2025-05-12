from django.contrib import admin

from .models import Rappel, Alerte

admin.site.register([Rappel, Alerte])
# Register your models here.
