from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from .forms import *
from .models import *
# Create your views here.
def inicio_view (request):
	return render(request, 'index.html', locals())

def vista_about(request):
    return render(request,'about.html')

def administrador_view(request):
    if request.user.is_authenticated and request.user.is_superuser:
         return render(request,'administrador.html')

def vista_login (request):
    usu = ""
    cla = ""
    if request.method == "POST":
        formulario = login_form(request.POST)
        if formulario.is_valid():
            usu = formulario.cleaned_data['usuario']
            cla = formulario.cleaned_data['clave']
            usuario = authenticate(username= usu, password = cla)
            if usuario is not None and usuario.is_active:
                login(request,usuario)
                return redirect('administrador')
            else:
                msj = "usuario o clave incorrectos"
    
    formulario = login_form()
    return render (request,'login.html',locals())
def vista_logout (request):
    logout(request)
    return redirect('/login/')

def lista_planes_view (request):
    listaP = Plan.objects.filter(status = True)
    return render(request, 'lista_planes.html',locals())

def ver_plan_view (request, id_plan):
    try:
        plan = Plan.objects.get(id = id_plan)
    except:
        print("el plan no existe")
        msj = "el plan no existe"
    return render(request,'ver_plan.html',locals())

def lista_turistas_view (request):
    listaT = Turista.objects.filter()
    return render(request, 'lista_turista.html',locals())
