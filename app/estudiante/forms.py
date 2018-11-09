from django import forms
from app.modelo.models import Usuario

class FormularioUsuario(forms.ModelForm):
    class Meta:
        model= Usuario
        fields = ["cedula", "nombres", "apellidoPaterno","apellidoMaterno","Sexo", "estado"]
