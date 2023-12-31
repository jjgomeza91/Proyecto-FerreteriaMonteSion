# Generated by Django 4.1.7 on 2023-11-28 01:20

import compras.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_bodega', models.CharField(max_length=45, verbose_name='Nombre bodega')),
                ('descripcion_bodega', models.CharField(max_length=200, verbose_name='Descripción bodega')),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_proveedor', models.CharField(max_length=45, verbose_name='Nombre proveedor')),
                ('tipo_documento', models.CharField(choices=[('CC', 'Cédula'), ('NI', 'Nit')], max_length=2, verbose_name='Tipo documento')),
                ('documento', models.PositiveIntegerField(unique=True, verbose_name='Número documento')),
                ('ciudad', models.CharField(max_length=45, verbose_name='Ciudad')),
                ('direccion', models.CharField(max_length=45, verbose_name='Dirección')),
                ('telefono', models.PositiveIntegerField(verbose_name='Teléfono')),
                ('nombre_contacto', models.CharField(max_length=45, verbose_name='Nombre contacto')),
                ('telefono_contacto', models.PositiveIntegerField(verbose_name='Teléfono contacto')),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=45, verbose_name='Nombre producto')),
                ('unidad_medida', models.CharField(max_length=45, verbose_name='Unidad medida')),
                ('stock_minimo', models.PositiveIntegerField(verbose_name='Stock mínimo')),
                ('precio_unitario_compra', models.PositiveIntegerField(verbose_name='Precio unitario compra')),
                ('precio_unitario_venta', models.PositiveIntegerField(verbose_name='Precio unitario venta')),
                ('imagen', models.ImageField(blank=True, default='compras/imagenProducto.jpg', null=True, upload_to=compras.models.get_image_filename)),
                ('estado', models.BooleanField(default=True)),
                ('bodega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras.bodega', verbose_name='Bodega')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras.proveedor', verbose_name='Proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=15, verbose_name='Código de Factura')),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('descuento', models.PositiveIntegerField(default=0, verbose_name='Descuento')),
                ('estado', models.CharField(choices=[('1', 'Abierta'), ('2', 'Anulada'), ('0', 'Cerrada')], default='1', max_length=1, verbose_name='Estado')),
                ('observaciones', models.TextField(blank=True, null=True, verbose_name='Observaciones')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras.proveedor', verbose_name='Proveedor')),
            ],
        ),
    ]
