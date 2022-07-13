from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    return render(request, 'registration/pagina_cadastro.html', {})

def base(request):
    return render(request, 'home/base.html', {})

#@login_required(login_url='/')
def home(request):
    return render(request, 'home/home.html', {})

def menubar(request):
    return render(request, 'home/menubar.html', {})

def sidebar(request):
    return render(request, 'home/sidebar.html', {})

def explorar(request):
    return render(request, 'home/explorar.html', {})

