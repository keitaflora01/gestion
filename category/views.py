from django.shortcuts import render

# Create your views here.
def categorie(request):
    return render(request, 'categorie.html')

def budget(request):
    return render(request, 'budgetform.html')

