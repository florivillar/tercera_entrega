# Create your views here.

from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from .forms import PostForm, DestinoForm, ComunidadForm, SearchForm
from .models import Post, Destino, Comunidad

def search_results(request):
    form = SearchForm(request.GET or None)
    results = {}
    query = None
    if form.is_valid():
        query = form.cleaned_data.get('query')

        if query:
            post_results = Post.objects.filter(
                Q(titulo_icontains=query) | Q(contenido_icontains=query))
            destino_results = Destino.objects.filter(
                Q(nombre__icontains=query))
            comunidad_results = Comunidad.objects.filter(
                Q(nombre__icontains=query))

            results = {
                'posts': post_results,
                'destinos': destino_results,
                'comunidades': comunidad_results,
            }

    return render(request, 'search_results.html', {'form': form, 'results': results, 'query': query})

def search_form(request):
    return render(request, 'search_form.html')

def inicio(request):
    return render(request, 'inicio.html')

def lista_posts(request):
    posts = Post.objects.all()
    return render(request, 'lista_posts.html', {'posts': posts})

def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_posts')
    else:
        form = PostForm()
    return render(request, 'crear_post.html', {'form': form})

def lista_destinos(request):
    destinos = Destino.objects.all()
    return render(request, 'lista_destinos.html', {'destinos': destinos})

def crear_destino(request):
    if request.method == "POST":
        form = DestinoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_destinos')
    else:
        form = DestinoForm()
    return render(request, 'crear_destino.html', {'form': form})

def lista_comunidades(request):
    comunidades = Comunidad.objects.all()
    return render(request, 'lista_comunidades.html', {'comunidades': comunidades})

def crear_comunidad(request):
    if request.method == "POST":
        form = ComunidadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_comunidades')
    else:
        form = ComunidadForm()
    return render(request, 'crear_comunidad.html', {'form': form})

