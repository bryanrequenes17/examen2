from django import forms
from exa1.modelo.models import Estudiantes

class FormularioEstudiante(forms.ModelForm):
    class Meta:
        model = Estudiantes
        fields = ["cedula", "nombres", "apellidos","edad", "genero","direccion"]