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
    path('lista_turistas/',lista_turistas_view, name = 'lista_turistas'),

]