from django import forms 
from .models import Categorydepense
from .models import CategoryRevenue


class CategoryDepenseForm(forms.ModelForm):
    class Meta:
        model = Categorydepense
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'name': 'Nom de la catégorie',
            'description': 'Description',
        }

class CategoryRevenueForm(forms.ModelForm):
    class Meta:
        model = CategoryRevenue
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'name': 'Nom de la catégorie',
            'description': 'Description',
        }        