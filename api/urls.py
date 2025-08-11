from django.urls import path
from .views import produit_api_view

urlpatterns = [
    path('chat/', produit_api_view, name='chat-api'),  # URL plus descriptive
    path('api/chat/', produit_api_view, name='api-chat'),  # Alternative avec préfixe API
    
]
