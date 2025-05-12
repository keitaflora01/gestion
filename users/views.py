from django.shortcuts import render
from django.contrib.auth.models import User
from .models import UserProfil

# Create your views here.
def connexion(request):
    return render(request,'connexion.html')
def inscription(request):
    if request.method =='POST':
        username = request.POST['username']
        nomComplet = request.POST['nomComplet']
        password = request.POST['password']
        email = request.POST['email']
        telephone = request.POST['telephone']
        adresse = request.POST['adresse']
        ville = request.POST['ville']
        revenuAnnuel = request.POST['revenuAnnuel']
        statutProfessionnel = request.POST['statutProfessionnel']
        situationFamiliale = request.POST['situationFamiliale']
        objectifFinancier = request.POST['objectifFinancier']
        imagePersonnalisee = request.POST['imagePersonnalisee']
        commentaires = request.POST['commentaires']

        user = User.objects.create_user(username=username, password=password)
        if user:
            userprofile = UserProfil.objects.create(user=user,name=username,fullname=nomComplet, email= email,telephone=telephone,password=password, situationfamiliale=situationFamiliale,ville=ville,revenueannuel=revenuAnnuel,objectiffinanciaire=objectifFinancier, commentaire=commentaires)

        print(nomComplet,adresse,telephone,ville,revenuAnnuel,statutProfessionnel,situationFamiliale,objectifFinancier,imagePersonnalisee,commentaires)
    return render(request,'inscription.html')
