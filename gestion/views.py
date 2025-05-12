from django.shortcuts import render 

def acceuil(request):
    return render(request, 'acceuil.html')
def tableaubord(request):
    return render(request,'tableaubord/tableaubord.html')

def depense(request):
    return render(request, 'tableaubord/depense/depensetableau.html')
def revenue(request):
    return render(request, 'tableaubord/revenue/revenuetableau.html')