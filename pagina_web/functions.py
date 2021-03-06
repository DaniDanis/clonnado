from multiprocessing import context
import os
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import form_TextoPost
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .functions import *
import json
import requests

# funcao que importa dados da API DE NOTICIA
def sidebar(url):  
    
    headers = {"Ocp-Apim-Subscription-Key" : '19a984ff47ec4a20acd1cf0657be1e42'}
    params  = {"mkt": "pt-BR", "q": "", "textDecorations": True, "textFormat": "HTML", "count": 100, "cc": "BR"}
    
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    search_results = json.dumps(response.json())
    data = json.loads(search_results)
    article = data['value']
    return article  

# retorna o NÚMERO de ~POSTS que pode ter na página
def limite_posts(lista_de_objetos_post):
    if len(lista_de_objetos_post) >= 17:
        n = 17
    else:
        n = len(lista_de_objetos_post)
    return n

# verifica se é um ~POST e se for salva no ~BANCO DE DADOS
def verifica_se_eh_post_e_salva(request, banco_user, banco_posts):
    if request.method == 'POST':
        user= banco_user.objects.get(id = request.user.id)
        banco_posts.objects.create(user=user,texto = request.POST['text-input'] ).save()
        
# Retorna lista do id todos os POSTS curtidos pelo usuário
def retorna_lista_de_posts_curtidos(request, banco_PostLike, ):
   lista_de_posts = [] 
   for i in banco_PostLike.objects.filter(user_id = request.user.id):
        lista_de_posts.append(i.post)
   return  lista_de_posts

# Insere POST no POSTLIKE BANCO DE DADOS
def crud_postlike(request):
    post_id = json.loads(request.body)['post_id']
    post = Posts.objects.get(id = post_id)
    if PostLike.objects.filter(user = request.user, post = post):
        PostLike.objects.get(post=post, user=request.user).delete()
    else:
        PostLike.objects.create(user=request.user, post=post).save()
