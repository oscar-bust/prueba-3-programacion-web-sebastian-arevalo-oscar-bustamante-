"""
URL configuration for prueba3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('', views.mostrar_index, name='index'),
    path('registrarse.html/', views.mostrar_regis, name='registrarse'),
    path('carrito.html/', views.mostrar_carrito, name='carro'),
    path('herramientas.html/', views.mostrar_herramientas, name='herramientas'),
    path('jardineria.html/', views.mostrar_jardineria, name='jardineria'),
    path('nostros.html/', views.mostrar_nosotros, name='nosotros'),
    path('sesion.html/', views.mostrar_sesion, name='sesion'),
    
    path('carrito/', views.carrito_list, name='carrito_list'),
    path('carrito/add/', views.carrito_add, name='carrito_add'),
    path('carrito/<int:pk>/update/', views.carrito_update, name='carrito_update'),
    path('carrito/<int:pk>/delete/', views.carrito_delete, name='carrito_delete'),


    

    
]

