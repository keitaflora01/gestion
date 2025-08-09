from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from category.models import *
from django.contrib.auth.decorators import login_required
from .models import Categorydepense,CategoryRevenue
from .forms import CategoryDepenseForm,CategoryRevenueForm 


# Create your views here.
def categoriedepense(request):
    user =request.user

    # if user:
    categories = Categorydepense.objects.filter(user=user)
    context = {
        'categorie': categories,
    }
    return render(request,'tableaubord/categorie/categorieDepense.html',context)    

def ajouterCategorieDepense(request):
    user=request.user
    if request.method == 'POST':
        categorie = request.POST['categorie']
        description = request.POST['description']
        categories = Categorydepense.objects.filter(user=user)
        nomsDesCategories = [c.name for c in categories]
        
        if categorie in nomsDesCategories:
            messages.error(request, "cette categorie existe deja")
        else:
            categorie = Categorydepense.objects.create(user=user,name=categorie , description=description)
            messages.success(request, "Catégorie enregistrée avec succès")
            return redirect('categoriedepense')
    
    return render(request,'tableaubord/categorie/ajoutercategorieDepense.html')



def modifiercategoriedepense(request, categorie_id):
    categorie = get_object_or_404(Categorydepense, id=categorie_id, user=request.user)
    
    if request.method == 'POST':
        form = CategoryDepenseForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
            messages.success(request, 'Catégorie modifiée avec succès!')
            return redirect('categoriedepense') 
    else:
        form = CategoryDepenseForm(instance=categorie)
    
    context = {
        'form': form,
        'categorie': categorie
    }
    return render(request, 'tableaubord/categorie/modifiercategoriedepense.html', context)

def supprimercategoriedepense(request, categorie_id):
    categorie = get_object_or_404(Categorydepense, id=categorie_id, user=request.user)
    
    if request.method == 'POST':
        categorie.delete()
        messages.success(request, 'Catégorie supprimée avec succès!')
        return redirect('categoriedepense')

    return redirect('categoriedepense')



    
def categorierevenue(request):
    categories = CategoryRevenue.objects.all()
    context = {
        'categorie': categories,
    }
    return render(request,'tableaubord/categorie/categorieRevenue.html',context)


def ajouterCategorieRevenue(request):
    user=request.user
    if request.method == 'POST':
        categorie = request.POST['categorie']
        description = request.POST['description']
        categories = CategoryRevenue.objects.filter(user=user)
        print(categories)
        nomsDesCategories = [c.name for c in categories]
        
        if categorie in nomsDesCategories:
            messages.error(request, "cette categorie existe deja")
        else:
            categorie = CategoryRevenue.objects.create(user=user,name=categorie , description=description)
            messages.success(request, "Catégorie enregistrée avec succès")
            return redirect('categorierevenue')
    
    return render(request,'tableaubord/categorie/ajoutercategorieRevenue.html')

def modifiercategorieRevenue(request, categorie_id):
    categorie = get_object_or_404(CategoryRevenue, id=categorie_id, user=request.user)
    
    if request.method == 'POST':
        form = CategoryRevenueForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
            messages.success(request, "La catégorie a été modifiée avec succès.")
            return redirect('categorierevenue') 
    else:
        form = CategoryRevenueForm(instance=categorie)
    
    context = {
        'form': form,
        'categorie': categorie,
        'title': 'Modifier une catégorie'
    }
    
    return render(request, 'tableaubord/categorie/modifiercategorieRevenue.html',context)


def supprimercategorierevenue(request, categorie_id):
    categorie = get_object_or_404(CategoryRevenue, id=categorie_id, user=request.user)
    
    if request.method == 'POST':
        categorie.delete()
        messages.success(request, 'Catégorie supprimée avec succès!')
        return redirect('categorierevenue')

    return redirect('categorierevenue')




