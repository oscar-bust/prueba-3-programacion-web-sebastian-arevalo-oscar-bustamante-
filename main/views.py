# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import  Carrito
from .forms import  CarritoForm















def mostrar_index(request):
    return render(request,'main/index.html')

def mostrar_regis(request):
    return render(request, 'main/registrarse.html')

def mostrar_carrito(request):
    return render(request, 'main/carrito.html')

def mostrar_herramientas(request):
    return render(request,'main/herramientas.html')

def mostrar_jardineria(request):
    return render(request,'main/jardineria.html')

def mostrar_nosotros(request):
    return render(request,'main/nostros.html')

def mostrar_sesion(request):
    return render(request,'main/sesion.html')




def carrito_add(request):
    if request.method == 'POST':
        
        nombre_producto = request.POST.get('nombre_producto')
        precio = request.POST.get('precio')
        cantidad = request.POST.get('cantidad')

     
        nuevo_carrito = Carrito(nombre_producto=nombre_producto, precio=precio, cantidad=cantidad)
        nuevo_carrito.save()


        return redirect('carrito_list')  

   
    return render(request, 'main/carrito_add.html')  



def carrito_list(request):
    carritos = Carrito.objects.all()
    return render(request, 'main/carrito_list.html', {'carritos': carritos}) 

def carrito_create(request):
    if request.method == 'POST':
        form = CarritoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('carrito_list')
    else:
        form = CarritoForm()
    return render(request, 'main/carrito_form.html', {'form': form})

def carrito_update(request, pk):
    carrito = get_object_or_404(Carrito, pk=pk)

    if request.method == 'POST':
        form = CarritoForm(request.POST, instance=carrito)
        if form.is_valid():
            form.save()
            return redirect('carrito_list')  # Redirige a la página del carrito
    else:
        form = CarritoForm(instance=carrito)
    return render(request, 'main/carrito_update.html', {'form': form})  # Renderiza la plantilla para modificar

def carrito_delete(request, pk):
    carrito = get_object_or_404(Carrito, pk=pk)
    if request.method == 'POST':
        carrito.delete()
        return redirect('carrito_list')  # Redirige a la página del carrito
    return render(request, 'main/carrito_confirm_delete.html', {'carrito': carrito})

