"""
URL configuration for yatra1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('home2/', views.home2),
    path('contact/', views.contact),
    # path('saveenquiry/', views.saveEnquiry, name="saveenquiry"),

    path('regis/', views.regis),
    path('login/', views.login),
    path('signin/', views.signin),
    path('goahony/', views.goahony),
    path('kerhony/', views.kerhony),
    path('simhony/', views.simhony),
    path('kashmir/', views.kashmir),
    path('orrisa/', views.orrisa),
    path('tamil/', views.tamil),
    path('assam/', views.assam),
    path('agra/', views.agra),
    path('kashmir/tourkasm/', views.tourkasm),
    path('kashmir/packagekasm/', views.packagekasm),
    path('kashmir/dayskasm/', views.dayskasm),
    path('kashmir/specialkasm/', views.specialkasm),
    path('kashmir/devikasmir/', views.devikasmir),
    path('mastourpak/', views.mastourpak),
    path('kastourpak/', views.kastourpak),
    path('jaitourpak/', views.jaitourpak),
    path('guwwild/', views.guwwild),
    path('sundarbanwild/', views.sundarbanwild),
    path('jaipurwild/', views.jaipurwild),
    path('popularand/', views.popularand),
    path('popularnainital/', views.popularnainital),
    path('chardham/', views.chardham),
    path('saveform/', views.saveform),
    path('index/', views.index),
    path('spinwheel/', views.spinwheel),
    path('res/', views.res),
    path('myjrny/', views.myjrny),
    path('newjrny/', views.newjrny),
    path('savepoint/', views.savepoint),
    path('nav/', views.nav),
    path('demo/', views.demo),
    path('wildlife/', views.wildlife),
   
   
     path('ladkh/', views.ladkh),
     path('goa/', views.goa),
     path('manali/', views.manali),
     path('vashno/', views.vashno),
     path('andaman/', views.andaman),
     path('nanital/', views.nanital),
     path('mussorie/', views.mussorie),
     path('udapur/', views.udapur),
     path('search/', views.search, name='search'),


   
]
