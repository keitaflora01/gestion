from django.urls import path
from .views import feedback

urlpatterns = [
    
    path('support/feedback/', feedback, name='feedback'),
]
