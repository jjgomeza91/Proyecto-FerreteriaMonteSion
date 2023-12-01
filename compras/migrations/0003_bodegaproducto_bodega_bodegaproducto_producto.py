# Generated by Django 4.2.7 on 2023-11-28 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0002_bodegaproducto_compradetalle'),
    ]

    operations = [
        migrations.AddField(
            model_name='bodegaproducto',
            name='bodega',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='compras.bodega', verbose_name='Bodega'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bodegaproducto',
            name='producto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='compras.producto', verbose_name='Producto'),
            preserve_default=False,
        ),
    ]
