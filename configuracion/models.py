from django.db import models
from django.utils.translation import gettext_lazy as _

def get_image_filename(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.documento}.{ext}"
    return f"configuracion/usuarios/{filename}"
# Create your models here.

class Usuario(models.Model):
    primer_nombre= models.CharField(max_length=45,verbose_name="Primer Nombre")
    segundo_nombre= models.CharField(max_length=45,verbose_name="Segundo Nombre", blank=True, null=True )

    primer_apellido= models.CharField(max_length=45,verbose_name="Primer Apellido")
    segundo_apellido= models.CharField(max_length=45,verbose_name="Segundo Apellido")

    fechaNacimiento= models.DateField(verbose_name="Fecha de Nacimiento")
    imagen = models.ImageField(upload_to=get_image_filename, blank=True, null=True,default="configuracion/imagenUsuario.jpg")

    class Rol(models.TextChoices):
        ADMINISTRADOR="AD",_("Administrador")
        VENDEDOR='VE',_("Vendedor")
        ALMACENISTA='AL',_("Almacenista")
    rol=models.CharField(max_length=2,choices=Rol.choices,verbose_name="Rol")


    direccion= models.CharField(max_length=45,verbose_name="Dirección")
    ciudad= models.CharField(max_length=45,verbose_name="Ciudad")
    telefono= models.PositiveIntegerField(verbose_name="Teléfono")
    
    class TipoDocumento(models.TextChoices):
        CEDULA='CC',_("Cédula")
        TARJETA='TI',_("Tarjeta de Identidad")
        CEDULA_EXTRANJERIA='CE',_("Cédula de Extrangería")
    tipo_documento= models.CharField(max_length=2,choices=TipoDocumento.choices,verbose_name="Tipo de Documento")
    documento= models.PositiveIntegerField(verbose_name="Documento", unique=True)
    
    estado= models.BooleanField(default=True)


    
    def clean(self):
        self.primer_nombre = self.primer_nombre.title()
    def __str__(self):
        return self.primer_nombre,self.primer_apellido
    class Meta:
        verbose_name_plural="Usuarios"


    @property
    def full_name(self):
        if self.segundo_nombre:
            return f"{self.primer_nombre} {self.segundo_nombre} {self.primer_apellido} {self.segundo_apellido}"
        else:
            return f"{self.primer_nombre} {self.primer_apellido} {self.segundo_apellido}"