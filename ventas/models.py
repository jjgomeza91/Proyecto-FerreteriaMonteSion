from django.db import models
from django.utils.translation import gettext_lazy as _

class Cliente(models.Model):
    nombre= models.CharField(max_length=45,verbose_name="Nombre")

    class TipoDocumento(models.TextChoices):
        CEDULA='CC',_("Cédula")
        TARJETA='TI',_("Tarjeta de Identidad")
        CEDULA_EXTRANJERIA='CE',_("Cédula de Extrangería")
    tipo_documento= models.CharField(max_length=2,choices=TipoDocumento.choices,verbose_name="Tipo de Documento")
    documento= models.PositiveIntegerField(verbose_name="Documento", unique=True)
    fecha_nacimiento= models.DateField(verbose_name="Fecha de Nacimiento")
    telefono= models.PositiveIntegerField(verbose_name="Teléfono")
    ciudad= models.CharField(max_length=45,verbose_name="Ciudad")
    direccion= models.CharField(max_length=45,verbose_name="Dirección")
    email= models.CharField(max_length=45,verbose_name="Email")
    estado= models.BooleanField(default=True)

