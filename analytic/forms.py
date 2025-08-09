from django import forms
from .models import Objectif

class ObjectifForm(forms.ModelForm):
    class Meta:
        model = Objectif
        fields = ['titre', 'categorie', 'montantcible', 'montantactuel', 'datelimite', 'description']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Vacances d\'été'}),
            'categorie': forms.Select(attrs={'class': 'form-control'}),
            'montantcible': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'placeholder': 'Montant à atteindre'}),
            'montantactuel': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'placeholder': 'Montant déjà épargné'}),
            'datelimite': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '4', 'placeholder': 'Décrivez votre objectif...'}),
        }
    
        