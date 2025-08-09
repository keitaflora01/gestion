from django import forms
from .models import Depense, Categorydepense
from .models import Revenue, CategoryRevenue

class DepenseForm(forms.ModelForm):
    class Meta:
        model = Depense
        fields = ['categorie', 'montant', 'datedepense', 'description']
        widgets = {
            'categorie': forms.Select(attrs={'class': 'form-control'}),
            'montant': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
            'datedepense': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'Décrivez votre dépense...'}),
        }
        labels = {
            'categorie': 'Catégorie',
            'montant': 'Montant (€)',
            'datedepense': 'Date',
            'description': 'Description',
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(DepenseForm, self).__init__(*args, **kwargs)
        # Si vous avez besoin de filtrer les catégories par utilisateur
        # if user:
        #     self.fields['categorie'].query
    
class RevenueForm(forms.ModelForm):
    class Meta:
        model = Revenue
        fields = ['categorie', 'montant', 'daterevenue', 'description']
        widgets = {
            'categorie': forms.Select(attrs={'class': 'form-control'}),
            'montant': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
            'daterevenue': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'Décrivez votre revenue...'}),
        }
        labels = {
            'categorie': 'Catégorie',
            'montant': 'Montant (€)',
            'daterevenue': 'Date',
            'description': 'Description',
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(RevenueForm, self).__init__(*args, **kwargs)
        # Si vous avez besoin de filtrer les catégories par utilisateur
        # if user:
        #     self.fields['categorie'].query    