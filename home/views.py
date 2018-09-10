from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from .forms import *
from .models import *
# Create your views here.
def inicio_view (request):
	return render(request, 'base.html', locals())

def vista_about(request):
    return render(request,'about.html')