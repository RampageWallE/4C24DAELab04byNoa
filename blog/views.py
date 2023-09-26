from django.shortcuts import render
from .models import Entrada, Autor

def lista_entradas(request):
    entradas = Entrada.objects.all()
    return render(request, 'blog/lista_entradas.html', {'entradas': entradas})

def lista_entradas_autor(request, nombre1:str):
    autor1 = Autor.objects.get(nombre=nombre1)
    entradas_autor = autor1.entrada_set.all()
    return render(request, 'blog/lista_entradas_autor.html', {'entradas': entradas_autor, 'nombre': nombre1})
