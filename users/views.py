from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
from .models import UserProfil
from django.contrib.auth import authenticate,login,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from notification.models import Rappel
from django.db.models import Q


# Create your views here.
def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password = password)
         
        if user is not None:
            if user.is_active:
                login(request, user)
                
                
                if  user.is_staff:
                
                    return redirect('dashbord')
                else:
                    userProfil=UserProfil.objects.filter(user=user)
                    
                
                    if UserProfil:
                        login(request, user)
                    return redirect('tableaubord')
            else :
                messages.error(request, "vous n'etes pas active")
                return redirect(request,'inscription')
        else:
            messages.error(request,"vous n'avez pas de compte utilisateur")
            return redirect('connexion')    


    return render(request,'connexion.html')

def inscription(request):
    if request.method =='POST':
        username = request.POST['username']
        nomComplet = request.POST['nomComplet']
        password = request.POST['password']
        email = request.POST['email']
        telephone = request.POST['telephone']
        revenuAnnuel = request.POST['revenuAnnuel']
        statutProfessionnel = request.POST['statutProfessionnel']
        objectifFinancier = request.POST['objectifFinancier']
        imagepersonnaliser = request.FILES['imagepersonnaliser']
        commentaires = request.POST['commentaires']


        print(imagepersonnaliser)

        user = User.objects.create_user(username=username, password=password)
        if user:
            userprofile = UserProfil.objects.create(
                user=user,
                name=username,
                fullname=nomComplet, 
                email= email,
                telephone=telephone,
                password=password, 
                revenueannuel=revenuAnnuel,
                objectiffinanciaire=objectifFinancier, 
                commentaire=commentaires,
                imagepersonnaliser=imagepersonnaliser,
                statutprofessionnel=statutProfessionnel,
            )

        print(nomComplet,telephone,revenuAnnuel,statutProfessionnel,objectifFinancier,imagepersonnaliser,commentaires)
        return redirect('connexion')
    return render(request,'inscription.html')

def deconnexion(request):
    logout(request)
    return redirect('connexion')

@login_required
def profil_utilisateur(request):
    
    user =request.user
    try:
        userprofile = UserProfil.objects.get(user=user)
    except UserProfil.DoesNotExist:
        messages.error(request, "votre profile utilisateur n'existe pas.")
        return redirect('inscription')    
    
    context = {
        'userprofile': userprofile,
        'user': user,
    }
    
    return render(request, 'tableaubord/profil_utilisateur.html', context)

@login_required
def utilisateurs(request):
    
    userProfil = UserProfil.objects.all()
    
    context = {
        'userprofils': userProfil
    }
    return render(request, 'administrateur/utilisateurs.html', context)

def allfeedback(request):
    messages = Rappel.objects.all().order_by('-date')
    total_message = messages.count()
    users_with_messages = messages.values('user').distinct().count()
    pending_messages = 0
    return render(request, 'administrateur/allfeedback.html', {
        'messages':messages,
        'total_message':total_message,
        'users_with_messages':users_with_messages,
        'pending_messages':pending_messages,
    
    })
    
# def rechercher(request, utilisateur_id):
#     query = request.GET.get('q','')
#     if query :
#        userProfil = UserProfil.objects.filter(
#            Q(name_icontains=query)|
#            Q(email_icontains=query)|
#            Q(date_icontains=query)
#        )
#     else :
#         userProfil = UserProfil.objects.all()
        
#     return render(request,'administrateur/utilisateurs.html', {query})       