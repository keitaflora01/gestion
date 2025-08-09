from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
from rapport.models import *

# Create your views here.
def rapport(request):
    
    
    return render(request,'tableaubord/rapport/rapport.html')
