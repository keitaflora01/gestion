from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from category.models import Categorydepense
from transactions.models import Depense
import requests
import json
import logging
from .models import ChatMessage
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)

@api_view(['GET', 'POST'])
@login_required
def produit_api_view(request):
    template_name = 'tableaubord/api/api.html'
    
    if request.method == 'GET':
        try:
            messages = ChatMessage.objects.filter(user=request.user).order_by('-created')
            return render(request, template_name, {'chats': messages})
        except Exception as e:
            logger.error(f"Error fetching messages: {str(e)}")
            return render(request, template_name, {'error': 'Error loading messages'})

    elif request.method == 'POST':
        try:
            data = request.data.get('prompt') or request.POST.get('prompt')
            if not data:
                messages = ChatMessage.objects.filter(user=request.user).order_by('-created')
                return render(request, template_name, {
                    'chats': messages,
                    'error': 'No prompt provided'
                })

            # Récupération des données financières
            try:
                depense = Depense.objects.filter(user=request.user).latest('date')
                montant = depense.montant
                categorie = depense.categorie.name if depense.categorie else "Non catégorisé"
                description = depense.description or "Aucune description"
            except Depense.DoesNotExist:
                montant = 0
                categorie = "Aucune donnée"
                description = "Aucune dépense enregistrée"

            # Construction du prompt pour Gemini
            prompt_text = f"""
            Données utilisateur:
            - Dernière dépense: {montant} FCFA
            - Catégorie: {categorie}
            - Description: {description}

            Contraintes:
            - Répondre uniquement aux questions sur la gestion financière
            - Pour les questions hors domaine, répondre: "Je ne peux répondre qu'aux questions sur la gestion financière."
            - Donner des réponses structurées et concises
            - Proposer des solutions pratiques personnalisées

            Question: {data}
            """

            # Appel à l'API Gemini
            api_key = "AIzaSyBxCguyZ4Hmeqedkr5-r7wgCT20F3MID1Y"
            endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
            
            response = requests.post(
                endpoint,
                headers={'Content-Type': 'application/json'},
                json={
                    "contents": [{
                        "parts": [{"text": prompt_text}]
                    }]
                }
            )

            if response.status_code == 200:
                ai_response = response.json()['candidates'][0]['content']['parts'][0]['text']
                
                # Enregistrement des messages
                ChatMessage.objects.create(
                    user=request.user,
                    message=data,
                    is_user=True
                )
                ChatMessage.objects.create(
                    user=request.user,
                    message=ai_response,
                    is_user=False
                )
                # Afficher tous les messages dans le template
                messages = ChatMessage.objects.filter(user=request.user).order_by('created')
                return render(request, template_name, {'chats': messages})
            else:
                messages = ChatMessage.objects.filter(user=request.user).order_by('created')
                return render(request, template_name, {
                   'chats': messages,
                   'error': 'API error'
                })   
           
                
        except Exception as e:
            logger.error(f"API error: {str(e)}")
            messages = ChatMessage.objects.filter(user=request.user).order_by('-created')
            return render(request, template_name, {
                'chats': messages,
                'error': str(e)
            })        
      # Si la méthode n'est ni GET ni POST
    messages = ChatMessage.objects.filter(user=request.user).order_by('-created')
    return render(request, template_name, {
        'chats': messages,
        'error': 'Méthode non supportée'
    })
