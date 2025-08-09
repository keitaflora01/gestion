# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from category.models import Categorydepense
# import requests
# import json
# from .models import ChatMessage


# # Create your views here.
# class ProduitAPIView(APIView):

#     templates_name = 'tableaubord/tableaubord.html'
    
#     def get(self, request):
#         allmessages = ChatMessage.objects.all()

#         return render(request, self.templates_name, {'chats':allmessages})
#         # categoriesList = Categorydepense.objects.all()
#         # list = []
#         # for categorie in categoriesList:
#         #     p = {
#         #         'name' : categorie.name,
#         #         'description' : categorie.description,
#         #     }
#         #     list.append(p)
            
#         # return render(request, self.template_name)
    
    
    
#     def post(self, request):
#         data = request.data['prompt']
#         api_key= "AIzaSyBxCguyZ4Hmeqedkr5-r7wgCT20F3MID1Y"
#         endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
#         header = {'Content-Type': 'application/json'}
#         payload  = {
#             "contents":[
#                 {
#                     "parts":[
#                         {
#                             'text':f"Mon site perle de la gestion des finances,tout les prompt qui seront pose doit etre de ce domaine.Si c'est hors du domaine,veuillez renvoyer le message 'je ne suis pas autoriser a repondre a cette question qui n'est pas du domaine gestion de finance.' prompt = {data}"
#                         }
#                     ]
#                 }
#             ]
#         }
#         try:
#             gemini_request = requests.post(
#                 url= endpoint,
#                 headers=header,
#                 data=json.dumps(payload)
#             )
#             if gemini_request.status_code ==200:
#                 r= gemini_request.json()
#                 resp = r['candidates'][0]['content']['parts'][0]['text']
#                 ChatMessage.objects.create(user = request.user, message = data, is_user=True)
#                 ChatMessage.objects.create(user= request.user, message =resp, is_user=False)

#                 allmessages = ChatMessage.objects.all()

#                 return render(request, self.templates_name, {'chats':allmessages})
            
        
#         except Exception as error:
#             print(error)

#             return Response('Failed')  
        
      
        



# from django.shortcuts import render, redirect
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from category.models import Categorydepense
# from transactions.models import Depense
# import requests
# import json
# import logging
# from .models import ChatMessage

# # Set up logging
# logger = logging.getLogger(__name__)

# # Create your views here.
# @api_view(['GET', 'POST'])
# def produit_api_view(request):
#     templates_name = 'tableaubord/api.html'
    
#     print("Hello world")
#     if request.method == 'GET':
#         allmessages = ChatMessage.objects.filter(user=request.user)
#         logger.info("GET request received: Loading dashboard with %d messages", allmessages.count())
#         return render(request, templates_name, {'chats': allmessages})
    
#     elif request.method == 'POST':
#         print(request.POST['prompt'])
#         try:
#             # Check if prompt exists in POST data or form data
#             if 'prompt' in request.data:
#                 data = request.data['prompt']
#                 print(data)
#             elif 'prompt' in request.POST:
#                 data = request.POST['prompt']
#             else:
#                 logger.error("No prompt found in request data: %s", request.POST)
#                 return render(request, templates_name, {
#                     'chats': ChatMessage.objects.all(),
#                     'error': 'No prompt provided'
#                 })
            
#             logger.info("Received prompt: %s", data)
            
#             # Updated API key
#             api_key = "AIzaSyBxCguyZ4Hmeqedkr5-r7wgCT20F3MID1Y"
#             endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
#             header = {'Content-Type': 'application/json'}
            
#             # recuperer les information
            
#             depense = Depense.objects.get(user = request.user)
#             categorie = Categorydepense.objects.filter(depense=depense).last()
            
#             montant = depense.montant
#             categorie = depense.categorie
#             description = depense.description
#             payload = {
#                 "contents": [
#                     {
#                         "parts": [
#                             {
#                                 'text': 
                                    
#                                     f"Depense: montant = {montant}, categorie = {categorie} , description = {description}.\n"
#                                     "Mon site parle de la gestion des finances,tout les prompt qui seront poser doit etre de ce domaine.Si c'est hors du domaine,veuillez renvoyer le message 'je ne suis pas autoriser a repondre a cette question qui n'est pas du domaine gestion de finance.'"
#                                     "Prédis le solde du mois prochain."
#                                     "tout prompt qui pose une question sur les categorie financier ,veuiller envoyer une reponse en recuperant ces "

#                                     "si l'utilisateur envoie un promt pour savoir comment gerer ces depenses ,en recuperant l'historique des depenses de l'utilisateur, donner des conseils personnalisés pour économiser, réduire les dépenses inutiles et saisir des opportunités d’économies selon son comportement actuel "       
#                                     "Voici les montants dépensés par mois par l'utilisateur :"
#                                     "si l'utilisateur envoie un promt pour savoir la prevision de ses depense, En te basant sur l'evolution de ses depense par rapport a ses revenues , dire combien cet utilisateur est-il susceptible de dépenser le mois prochain "
#                                     "donner de facon bref et tructurer les reponses aux clients tout en numerotant chaque etapes decrite "
#                                     "1.causes de ses depenses:(expliquer brievement les causes de ses depense)"
#                                     "2.les consequence:(dire l'impacte par raport a ces objectifs fixer)"
#                                     "3. les solutions pratique:(donner quelque solution en fonction de ses revenue )"
                                    
                                    
#                                     f"prompt = {data}"
#                             }
#                         ]
#                     }
#                 ]
#             }
            
#             logger.info("Sending request to Gemini API")
#             gemini_request = requests.post(
#                 url=endpoint,
#                 headers=header,
#                 data=json.dumps(payload)
#             )
            
#             logger.info("Gemini API response status: %d", gemini_request.status_code)
            
#             if gemini_request.status_code == 200:
#                 r = gemini_request.json()
#                 logger.debug("API Response: %s", r)
                
#                 resp = r['candidates'][0]['content']['parts'][0]['text']
                
#                 # Create user message
#                 ChatMessage.objects.create(user=request.user, message=data, is_user=True)
#                 logger.info("Created user chat message")
                
#                 # Create AI response message
#                 ChatMessage.objects.create(user=request.user, message=resp, is_user=False)
#                 logger.info("Created AI chat message")
                
#                 allmessages = ChatMessage.objects.all()
#                 return render(request, templates_name, {'chats': allmessages})
#             else:
#                 logger.error("Gemini API error: Status %d, Response: %s", 
#                             gemini_request.status_code, gemini_request.text)
#                 return render(request, templates_name, {
#                     'chats': ChatMessage.objects.all(),
#                     'error': f'API Error: {gemini_request.status_code}'
#                 })
        
#         except Exception as error:
#             logger.exception("Error processing chat request: %s", str(error))
#             allmessages = ChatMessage.objects.all()
#             return render(request, templates_name, {
#                 'chats': allmessages,
#                 'error': f'Error: {str(error)}'
#             })



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
