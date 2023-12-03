from django.shortcuts import render, redirect
from .models import Tours
from django.contrib import messages

# Create your views here.
def home(request):
    tours = Tours.objects.all()
    # messages.success(request, 'Tours Listados!')
    return render(request, "gestionTours.html", {"tours": tours})

def registrarTours(request):
    codigo=request.POST['txtCodigo']
    circuito=request.POST['txtCircuito']
    descripcion=request.POST['txtDescripcion']
    aereo=request.POST['txtAereo']
    traslados=request.POST['txtTraslados']
    comidas=request.POST['txtComidas']

    tours = Tours.objects.create(
        codigo=codigo, circuito=circuito, descripcion=descripcion, aereo=aereo, traslados=traslados, comidas=comidas)
    messages.success(request, 'Tours Registrados!')
    return redirect('/') 

def edicionTours(request, codigo):
    tours = Tours.objects.get(codigo=codigo)
    return render(request, "edicionTours.html", {"tours": tours})


def editarTours(request):
    codigo=request.POST['txtCodigo']
    circuito=request.POST['txtCircuito']
    descripcion=request.POST['txtDescripcion']
    aereo=request.POST['txtAereo']
    traslados=request.POST['txtTraslados']
    comidas=request.POST['txtComidas']

    tours = Tours.objects.get(codigo=codigo)
    tours.circuito = circuito
    tours.descripcion = descripcion
    tours.aereo = aereo
    tours.traslados = traslados
    tours.comidas = comidas
    tours.save()

    messages.success(request, '¡Tour actualizado!')

    return redirect('/')


def eliminarTours(request, codigo):
    tours = Tours.objects.get(codigo=codigo)
    tours.delete()

    messages.success(request, '¡Tour eliminado!')

    return redirect('/')
