# Generated by Django 4.2.3 on 2023-08-04 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.CharField(choices=[('cédula', 'Cédula'), ('ruc', 'RUC'), ('pasaporte', 'Pasaporte')], max_length=20)),
                ('documento_detalle', models.IntegerField(default=1000000000, verbose_name='Número de cédula')),
                ('apellido', models.CharField(max_length=50)),
                ('dirección', models.CharField(max_length=100)),
                ('teléfono', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('código', models.IntegerField(primary_key=True, serialize=False)),
                ('descripción', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.FloatField()),
                ('stock', models.IntegerField()),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('número', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(auto_now=True)),
                ('cantidad', models.IntegerField()),
                ('observaciones', models.CharField(max_length=50, verbose_name='Observaciones de la venta')),
                ('iva', models.FloatField(choices=[(0.12, '12%')])),
                ('descuento', models.FloatField(choices=[(0.1, '10%'), (0.2, '20%'), (0.3, '30%')])),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.cliente')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.producto')),
            ],
        ),
    ]
