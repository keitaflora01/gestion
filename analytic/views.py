from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Objectif, ObjectifComplete
from datetime import datetime
from .forms import ObjectifForm

# Create your views here.
def budget(request):
    return render(request, 'budgetform.html')

def objectif(request):
    user = request.user
    objectifs = Objectif.objects.filter(user=user)
    objectifs_completes = ObjectifComplete.objects.filter(user=user).order_by('-date_achievement')
    
    context = {}
    objs = []
    
    # Variables pour les statistiques
    objectifs_en_cours = 0
    objectifs_atteints = 0
    objectifs_en_retard = 0
    progression_totale = 0
    
    today = datetime.now().date()

    for objectif in objectifs:
        try:
            montant_actuel = float(objectif.montantactuel)
            montant_cible = float(objectif.montantcible)
            date_limite = objectif.datelimite

            if montant_cible > 0:
                pourcentage = (montant_actuel / montant_cible) * 100
                pourcentage_valeur = min(100, pourcentage)  # Limiter à 100% maximum
            else:
                pourcentage = 0
                pourcentage_valeur = 0

            # Déterminer la couleur en fonction du pourcentage
            if pourcentage_valeur < 25:
                couleur = "danger"
            elif pourcentage_valeur < 50:
                couleur = "warning"
            elif pourcentage_valeur < 75:
                couleur = "info"
            else:
                couleur = "success"
            
            # Vérifier le statut de l'objectif
            if pourcentage >= 100:
                # Objectif atteint (100%)
                objectifs_atteints += 1
            elif date_limite < today:
                # Objectif en retard (date dépassée et pas 100%)
                objectifs_en_retard += 1
            else:
                # Objectif en cours
                objectifs_en_cours += 1

            progression_totale += pourcentage_valeur

            obj = {
                "id": objectif.id,
                "titre": objectif.titre,
                "categorie": objectif.categorie,
                "montantcible": objectif.montantcible,
                "montantactuel": objectif.montantactuel,
                "datelimite": objectif.datelimite,
                "description": objectif.description,
                "pourcentage": f"{round(pourcentage_valeur, 2)}%",
                "pourcentage_valeur": pourcentage_valeur,
                "couleur_progression": couleur,
            }

            objs.append(obj)
        except (ValueError, TypeError) as e:
            # Gérer les erreurs de conversion
            continue

    context['objectifs'] = objs
    context['objectifs_completes'] = objectifs_completes
    
    # Calcul des statistiques
    context['nombre_objectifs_en_cours'] = objectifs_en_cours
    context['nombre_objectifs_atteints'] = objectifs_atteints
    context['nombre_objectifs_en_retard'] = objectifs_en_retard
    
    # Calcul de la progression moyenne
    total_objectifs = objectifs_en_cours + objectifs_en_retard + objectifs_atteints
    if total_objectifs > 0:
        progression_moyenne = progression_totale / total_objectifs
        context['progression_moyenne'] = f"{round(progression_moyenne)}%"
    else:
        context['progression_moyenne'] = "0%"
    
    # Préparation des données pour le graphique
    graph_labels = []
    graph_data = []
    graph_colors = []
    graph_background_colors = []

    for obj in objs:
        graph_labels.append(obj['titre'])
        graph_data.append(obj['pourcentage_valeur'])
        if obj['pourcentage_valeur'] < 25:
            color = '#f72585'
        elif obj['pourcentage_valeur'] < 50:
            color = '#f8961e'
        elif obj['pourcentage_valeur'] < 75:
            color = '#4895ef'
        else:
            color = '#4cc9f0'
        graph_colors.append(color)
        graph_background_colors.append(f"{color}30")

    context['graph_labels'] = graph_labels
    context['graph_data'] = graph_data
    context['graph_colors'] = graph_colors
    context['graph_background_colors'] = graph_background_colors
    
    return render(request, 'tableaubord/objectif/objectif.html', context)

def ajouterobjectif(request):
    user = request.user
    if request.method == 'POST':
        titre = request.POST['titre']
        categorie = request.POST['categorie']
        montantcible = request.POST['montantcible']
        montantactuel = request.POST['montantactuel']
        datelimite = request.POST['datelimite']
        description = request.POST['description']
        
        # Créer l'objectif
        objectif = Objectif.objects.create(
            user=user,
            titre=titre,
            categorie=categorie,
            montantcible=montantcible,
            montantactuel=montantactuel,
            datelimite=datelimite,
            description=description
        )
        
        # Vérifier si l'objectif est déjà atteint à la création
        try:
            montant_actuel = float(montantactuel)
            montant_cible = float(montantcible)
            
            if montant_cible > 0 and montant_actuel >= montant_cible:
                # Créer un objectif complété directement
                ObjectifComplete.objects.create(
                    user=user,
                    titre=titre,
                    categorie=categorie,
                    montant=montant_cible,
                    date_achievement=datetime.now()
                )
                
                # Supprimer l'objectif en cours
                objectif.delete()
                
                messages.success(request, f"L'objectif '{titre}' a été créé et directement atteint ! Il a été ajouté aux objectifs complétés.")
            else:
                messages.success(request, "Objectif enregistré avec succès")
        except (ValueError, TypeError):
            messages.success(request, "Objectif enregistré avec succès")
        
        return redirect('objectif')
     
    return render(request, 'tableaubord/objectif/ajouterobjectif.html')

def modifierobjectif(request, objectif_id):
    objectif = get_object_or_404(Objectif, id=objectif_id, user=request.user)
    
    if request.method == 'POST':
        form = ObjectifForm(request.POST, instance=objectif)
        if form.is_valid():
            objectif = form.save()
            
            # Vérifier si l'objectif est maintenant atteint
            try:
                montant_actuel = float(objectif.montantactuel)
                montant_cible = float(objectif.montantcible)
                
                if montant_cible > 0 and montant_actuel >= montant_cible:
                    # Créer un objectif complété
                    ObjectifComplete.objects.create(
                        user=request.user,
                        titre=objectif.titre,
                        categorie=objectif.categorie,
                        montant=montant_cible,
                        date_achievement=datetime.now()
                    )
                    
                    # Supprimer l'objectif en cours
                    objectif.delete()
                    
                    messages.success(request, f"Félicitations ! L'objectif '{objectif.titre}' est maintenant atteint et a été déplacé vers les objectifs complétés.")
            except (ValueError, TypeError):
                pass
                
            return redirect('objectif')
    else:
        form = ObjectifForm(instance=objectif)
    
    return render(request, 'tableaubord/objectif/modifierobjectif.html', {'form': form, 'objectif': objectif})

def supprimerobjectif(request, objectif_id):
    objectif = get_object_or_404(Objectif, id=objectif_id, user=request.user)
    
    if request.method == 'POST':
        objectif.delete()
        return redirect('objectif')
    
    return render(request, 'tableaubord/objectif/supprimerobjectif.html', {'objectif': objectif})