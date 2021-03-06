"""clonnado_twiter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.views.generic.base import RedirectView
from . import views, functions

urlpatterns = [    
    path('base/', views.base),
    path("home/", views.home, name="home"),
    path("explorar/", views.explorar, name="explorar"),
    path('login/', views.login, name="login"),
    path("sidebar/", views.sidebar, name='sidebar'),
    path('', RedirectView.as_view(url='home')),
    path('curtir-action/',views.curtir_action, name="curtir-action"),
    path('tocomment/', views.tocomment,  name="paginaweb.tocomment"),
    path('details/<int:post_id>/', views.postdetails, name="paginaweb.post_details"),
]