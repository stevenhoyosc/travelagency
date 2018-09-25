from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio_view, name='inicio'),
    path('about/',vista_about, name = 'about'),
    path('login/',vista_login, name = 'login'),
    path('logout/',vista_logout,name = 'logout'),
    path('lista_planes/',lista_planes_view, name = 'lista_planes'),
    path('ver_plan/<int:id_plan>/',ver_plan_view, name = 'ver_plan'),
    path('administrador/',administrador_view, name = 'administrador'),
    path('lista_turista/',lista_turista_view, name = 'lista_turista'),
    path('lista_comprador/',lista_comprador_view, name = 'lista_comprador'),
    
    path('contratovuelo/',contratovuelo_view, name = 'contratovuelo'),
    path('vuelos/',vuelos_view, name = 'vuelos'),
    path('reservaciones/',reservaciones_view, name = 'reservaciones'),
    path('hoteles/',hoteles_view, name = 'hoteles'),
    path('contratosucursal/',contratosucursal_view, name = 'contratosucursal'),
    path('sucursales/',sucursales_view, name = 'sucursales'),
]