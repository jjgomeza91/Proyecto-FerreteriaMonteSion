from django.forms import ModelForm, widgets
from ventas.models import Cliente


class ClienteForm(ModelForm):
    class Meta:
        model= Cliente
        fields= "__all__"
        exclude=["estado"]
        widgets={
            'fechaNacimiento':widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d')
        }

