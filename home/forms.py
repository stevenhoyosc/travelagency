from django import forms
from .models import *
from django.contrib.auth.models import User

class login_form(forms.Form):
    usuario = forms.CharField(widget = forms.TextInput())
    clave   = forms.CharField(widget = forms.PasswordInput(render_value=False))