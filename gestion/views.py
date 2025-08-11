from django.shortcuts import render
from django.db.models import Sum
from datetime import datetime, timedelta
from transactions.models import Depense, Revenue
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test


def acceuil(request):
    return render(request, 'acceuil.html')

def is_admin(user):
    return user.is_superuser or user.is_staff

@user_passes_test(is_admin, login_url='/login/')
def dashbord(request):
    return render(request,'administrateur/dashbord.html')

def tableaubord(request):
    user = request.user
    
    # Calcul des statistiques du mois courant
    current_month = datetime.now().month
    current_year = datetime.now().year
    
    # Revenus et dépenses du mois courant
    revenus_mois = Revenue.objects.filter(
        user=user,
        daterevenue__month=current_month,
        daterevenue__year=current_year
    ).aggregate(total=Sum('montant'))['total'] or 0
    
    depenses_mois = Depense.objects.filter(
        user=user,
        datedepense__month=current_month,
        datedepense__year=current_year
    ).aggregate(total=Sum('montant'))['total'] or 0
    
    # Données pour le graphique de comparaison (6 derniers mois)
    months_data = []
    for i in range(5, -1, -1):  # 5 mois précédents + mois courant
        date = datetime.now() - timedelta(days=30*i)
        month = date.month
        year = date.year
        
        revenus = Revenue.objects.filter(
            user=user,
            daterevenue__month=month,
            daterevenue__year=year
        ).aggregate(total=Sum('montant'))['total'] or 0
        
        depenses = Depense.objects.filter(
            user=user,
            datedepense__month=month,
            datedepense__year=year
        ).aggregate(total=Sum('montant'))['total'] or 0
        
        months_data.append({
            'month': date.strftime("%B %Y"),
            'revenus': revenus,
            'depenses': depenses
        })
    
    # Données pour le graphique des tendances (4 dernières semaines)
    trend_data = []
    for i in range(3, -1, -1):  # 4 dernières semaines
        start_date = datetime.now() - timedelta(weeks=i+1)
        end_date = datetime.now() - timedelta(weeks=i)
        
        depenses = Depense.objects.filter(
            user=user,
            datedepense__gte=start_date,
            datedepense__lt=end_date
        ).aggregate(total=Sum('montant'))['total'] or 0
        
        trend_data.append({
            'week': f"Semaine {4-i}",
            'depenses': depenses
        })
    
    context = {
        'chart_data': months_data,
        'trend_data': trend_data,
        'current_month': {
            'revenus': revenus_mois,
            'depenses': depenses_mois
        }
    }
    
    return render(request, 'tableaubord/tableaubord.html', context)




def stats_api(request):
    user = request.user
    months = int(request.GET.get('months', 6))
    
    data = []
    for i in range(months-1, -1, -1):
        date = datetime.now() - timedelta(days=30*i)
        month = date.month
        year = date.year
        
        revenus = Revenue.objects.filter(
            user=user,
            daterevenue__month=month,
            daterevenue__year=year
        ).aggregate(total=Sum('montant'))['total'] or 0
        
        depenses = Depense.objects.filter(
            user=user,
            datedepense__month=month,
            datedepense__year=year
        ).aggregate(total=Sum('montant'))['total'] or 0
        
        data.append({
            'month': date.strftime("%B %Y"),
            'revenus': revenus,
            'depenses': depenses
        })
    
    return JsonResponse(data, safe=False)

def trends_api(request):
    user = request.user
    period = request.GET.get('period', 'month')
    
    if period == 'week':
        labels = []
        values = []
        for i in range(6, -1, -1):
            date = datetime.now() - timedelta(days=i)
            label = date.strftime("%A")
            total = Depense.objects.filter(
                user=user,
                datedepense__date=date.date()
            ).aggregate(total=Sum('montant'))['total'] or 0
            labels.append(label)
            values.append(total)
    elif period == 'year':
        labels = []
        values = []
        for i in range(11, -1, -1):
            date = datetime.now() - timedelta(days=30*i)
            label = date.strftime("%B")
            total = Depense.objects.filter(
                user=user,
                datedepense__month=date.month,
                datedepense__year=date.year
            ).aggregate(total=Sum('montant'))['total'] or 0
            labels.append(label)
            values.append(total)
    else: # month
        labels = []
        values = []
        for i in range(3, -1, -1):
            start_date = datetime.now() - timedelta(weeks=i+1)
            end_date = datetime.now() - timedelta(weeks=i)
            label = f"Semaine {4-i}"
            total = Depense.objects.filter(
                user=user,
                datedepense__gte=start_date,
                datedepense__lt=end_date
            ).aggregate(total=Sum('montant'))['total'] or 0
            labels.append(label)
            values.append(total)
    
    return JsonResponse({'labels': labels, 'values': values})
