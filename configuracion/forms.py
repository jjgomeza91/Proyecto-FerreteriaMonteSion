from django.forms import ModelForm, ModelChoiceField, widgets
from configuracion.models import Usuario


class UsuarioForm(ModelForm):
    class Meta:
        model= Usuario
        fields= "__all__"
        exclude=["estado","user"]
        widgets={
            'fechaNacimiento':widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d')
        }

class UsuarioEditarForm(ModelForm):
    class Meta:
        model= Usuario
        fields= "__all__"
        exclude=["estado","fechaNacimiento", "documento"]
        widgets={
            'fechaNacimiento':widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d')
        }
