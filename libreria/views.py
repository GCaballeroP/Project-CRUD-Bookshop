from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm
# Create your views here.

def inicio(request):
    return render(request,'paginas/inicio.html', {})

def nosotros(request):
    return render(request,'paginas/nosotros.html', {})

def libros(request):
    libros= Libro.objects.all()

    return render(request,'libros/index.html',{'libros':libros})

def create(request):
    form = LibroForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('libros')
    return render(request,'libros/create.html',{'form':form})

def edit(request,id):
    libro = Libro.objects.get(id=id)
    form = LibroForm(request.POST or None,request.FILES or None, instance = libro)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('libros')
    return render(request,'libros/edit.html', {'form': form})

def delete(request,id):
    libro=Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')