"""sunday URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import mainapp.views as mainapp
from django.contrib import admin
from django.urls import path
from django.urls import path, include

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('catalog/', mainapp.catalog, name='catalog'),
    path('catalog/category/<int:pk>/', mainapp.catalog_page, name='catalog_page'),
    path('basket/', mainapp.basket, name='basket'),
    path('secret/', mainapp.secret, name='secret'),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('sponsor/', include('sponsorapp.urls', namespace='sponsor')),
    path('computer/', include('computerapp.urls', namespace='computer')),
    path('week/', include('weekapp.urls', namespace='week')),
    path('location/', include('locationapp.urls', namespace='location')),


    path('admin/', admin.site.urls),
]
