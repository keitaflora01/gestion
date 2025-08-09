from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from users.models import *
from transactions.models import *
from .forms import DepenseForm,RevenueForm
from django.db.models import Q
from transactions.models import Depense, Revenue
from django.db.models import Sum
import datetime
import json
# Create your views here.

def depensetableau(request):

    user=request.user
    depense = Depense.objects.filter(user=user)
    print(depense)
    
    

    context = {
        'depenses' : depense,
    }
    return render(request, 'tableaubord/depense/depensetableau.html',context)

def ajouterdepense(request):
    user = request.user  # ✅ Correct assignment here

    categories = Categorydepense.objects.filter(user=user)
    context = {
        'categories': categories,
    }

    if request.method == 'POST':
        user = request.user  # ✅ Again, no comma here
        montant = request.POST['montant']
        datedepense = request.POST['date']
        description = request.POST['description']
        categorie_id = request.POST['categorie']

        categorie = Categorydepense.objects.get(pk=categorie_id)

        if categorie == "default":
            messages.error(request, "Veuillez choisir une catégorie valide.")
            return redirect('ajouterdepense')  # Or handle this better

        # ✅ Create the depense
        Depense.objects.create(
            user=user,
            categorie=categorie,
            montant=montant,
            datedepense=datedepense,
            description=description
        )

        return redirect('depensetableau')

    return render(request, 'tableaubord/depense/ajouterdepense.html', context)

def modifierdepense(request, depense_id):
    depense = get_object_or_404(Depense, id=depense_id, user=request.user)
    
    if request.method == 'POST':
        form = DepenseForm(request.POST, instance=depense, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "La dépense a été modifiée avec succès!")
            return redirect('depensetableau')
    else:
        form = DepenseForm(instance=depense, user=request.user)
    
    context = {
        'form': form,
        'depense': depense,
        'categories': Categorydepense.objects.all() 
    }
    return render(request, 'tableaubord/depense/modifierdepense.html', context)
def detaildepense(request, depense_id):
    depense = get_object_or_404(Depense, id=depense_id, user=request.user)
    context = {
        'depense': depense
    }
    return render(request, 'tableaubord/depense/detaildepense.html', context)

def supprimerdepense(request, depense_id):
    depense = get_object_or_404(Depense, id=depense_id, user=request.user)
    
    if request.method == 'POST':
        depense.delete()
        messages.success(request, "La dépense a été supprimée avec succès!")
        return redirect('depensetableau')
    
    context = {
        'depense': depense
    }
    return render(request, 'tableaubord/depense/supprimerdepense.html', context)

def recherchedepense(request, depense_id):
    query = request.GET.get('q','')
    if query :
        depense = Depense.objects.filter(
            Q(date_icontains=query)|
            Q(categorie_icontains=query)|
            Q(montant_icontains=query)
        )
    else :
        depense = Depense.objects.all()
        
        
    return render(request, 'tableaubord/depense/depensetableau.html', {query})        
     




def revenuetableau(request):

    user=request.user
    revenues = Revenue.objects.filter(user=user)
    print(revenues)

    context = {
        'revenues' : revenues,
    }
    return render(request, 'tableaubord/revenue/revenuetableau.html',context)

def ajouterrevenue(request):
    user = request.user  # ✅ Correct assignment here

    categories = CategoryRevenue.objects.filter(user=user)
    context = {
        'categories': categories,
    }

    if request.method == 'POST':
        user = request.user  # ✅ Again, no comma here
        montant = request.POST['montant']
        daterevenue = request.POST['date']
        description = request.POST['description']
        categorie_id = request.POST['categorie']

        categorie = CategoryRevenue.objects.get(pk=categorie_id)

        if categorie == "default":
            messages.error(request, "Veuillez choisir une catégorie valide.")
            return redirect('ajouterrevenue')  # Or handle this better

        # ✅ Create the revenue
        Revenue.objects.create(
            user=user,
            categorie=categorie,
            montant=montant,
            daterevenue=daterevenue,
            description=description
        )

        return redirect('revenuetableau')

    return render(request, 'tableaubord/revenue/ajouterrevenue.html', context)
def modifierrevenue(request, revenue_id):
    revenue = get_object_or_404(Revenue, id=revenue_id, user=request.user)
    
    if request.method == 'POST':
        form = RevenueForm(request.POST, instance=revenue, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "La revenue a été modifiée avec succès!")
            return redirect('revenuetableau')
    else:
        form = RevenueForm(instance=revenue, user=request.user)
    
    context = {
        'form': form,
        'revenue': revenue,
        'categories': CategoryRevenue.objects.all() 
    }
    return render(request, 'tableaubord/revenue/modifierrevenue.html', context)

def detailrevenue(request, revenue_id):
    revenue = get_object_or_404(Revenue, id=revenue_id, user=request.user)
    context = {
        'revenue': revenue
    }
    return render(request, 'tableaubord/revenue/detailrevenue.html', context)

def supprimerrevenue(request, revenue_id):
    revenue = get_object_or_404(Revenue, id=revenue_id, user=request.user)
    
    if request.method == 'POST':
        revenue.delete()
        messages.success(request, "La revenue a été supprimée avec succès!")
        return redirect('revenuetableau')
    
    context = {
        'revenue': revenue
    }
    return render(request, 'tableaubord/revenue/supprimerrevenue.html', context)


    