from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages



def index(request):
    productosAll = Producto.objects.all()
    data = {
        'listado': productosAll
    }
    return render(request, 'core/index.html', data)

def about(request):
    return render(request,('core/about.html'))

def blog(request):
    return render(request,('core/blog.html'))

def carrito(request):
    productosAll = Producto.objects.all()[:1]
    data = {
        'listado': productosAll
    }
    return render(request, 'core/carrito.html', data)

def checkout(request):
    return render(request,('core/checkout.html'))

def detalle(request):
    return render(request,('core/detalle.html'))

def sesion(request):
    return render(request,('core/sesion.html'))

def subscripcion(request):
    return render(request,('core/subscripcion.html'))

def oneProduct(request):
    data = {
        'form' : CantidadForm()
    }

    if request.method == 'POST':
        formulario = CantidadForm(request.POST, files=request.FILES) 
        if formulario.is_valid():
            formulario.save() 
            data['msj'] = "Producto guardado correctamente"
            messages.success(request, "Producto almacenado correctamente")


    return render(request, 'core/oneProduct.html', data)
 


def price(request):
    return render(request,('core/price.html'))

def product(request):
    productosAll = Producto.objects.all()
    data = {
        'listado': productosAll
    }
    return render(request, 'core/product.html', data)

def prue(request):
    carritosAll = Producto.objects.all()
    data = {
        'listado': carritosAll
    }
    return render(request,'core/prue.html', data)

def seguimiento(request):
    productosAll = Producto.objects.all()[:1]
    data = {
        'listado': productosAll
    }
    return render(request,'core/seguimiento.html', data)

def registrar(request):
    return render(request,('core/registrar.html'))

def service(request):
    return render(request,('core/service.html'))

def team(request):
    return render(request,('core/team.html'))
    
def testimonio(request):
    return render(request,('core/testimonio.html'))

#CRUD
def add(request):
    data = {
        'form' : ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES) 
        if formulario.is_valid():
            formulario.save() 
            data['msj'] = "Producto guardado correctamente"
            messages.success(request, "Producto almacenado correctamente")

    return render(request, 'core/addProduct.html', data)


def update(request,id):
    producto = Producto.objects.get(id=id)
    data = {
        'form' : ProductoForm(instance=producto) 
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            #data['msj'] = "Producto modificado correctamente"
            messages.success(request, "Producto modificado correctamente")
            data['form'] = formulario 

    return render(request, 'core/updateProduct.html', data)

def delete(request,id):
    producto = Producto.objects.get(id=id) 
    producto.delete()

    return redirect(to="index")

