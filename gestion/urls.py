from django.urls import path, include
from . import settings
from django.conf.urls.static import static

"""
URL configuration for gestion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import acceuil, tableaubord,dashbord,stats_api,trends_api
from django.contrib.auth.views import LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns




urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
    path('',acceuil),
    path('dashboard/',tableaubord, name='tableaubord'),
    path('dashbordadmin/', dashbord, name='dashbord'),
    path('dashboard/category/',include('category.urls')),
    path('dashboard/transactions',include('transactions.urls')),
    path('dashboard/objectif', include('analytic.urls')),
    path('api/', include('api.urls')),
    path('rapport/', include('rapport.urls')),
    path('api/stats/',stats_api, name='stats_api'),
    path('api/trends/',trends_api, name='trends_api'),
    path('logout/', LogoutView.as_view(next_page='connexion'), name='logout'),
    path('dashbordadmin/', dashbord, name='dashbord'),
    path('notification/', include('notification.urls')),
    
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

