from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio_view, name='inicio'),
    path('about/',vista_about),
]