# urls.py
from django.urls import path

from . import views


urlpatterns = [
    path('main/index.html', views.mostrar_index, name='index'),
    path('main/registrarse.html/', views.mostrar_regis, name='registrarse'),
    path('main/carrito.html/', views.mostrar_carrito, name='carro'),
    path('herramientas.html/', views.mostrar_herramientas, name='herramientas'),
    path('jardineria.html/', views.mostrar_jardineria, name='jardineria'),
    path('nostros.html/', views.mostrar_nosotros, name='nosotros'),
    path('sesion.html/', views.mostrar_sesion, name='sesion'),
    

    
    path('carrito/', views.carrito_list, name='carrito_list'),
    path('carrito/add/', views.carrito_add, name='carrito_add'),
    path('carrito/<int:pk>/update/', views.carrito_update, name='carrito_update'),
    path('carrito/<int:pk>/delete/', views.carrito_delete, name='carrito_delete'),
    path('carrito/crear/', views.carrito_create, name='carrito_create'),
]
