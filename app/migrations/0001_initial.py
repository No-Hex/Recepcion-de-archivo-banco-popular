# Generated by Django 4.0.4 on 2022-05-26 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('rnc', models.CharField(max_length=9, primary_key=True, serialize=False, unique=True)),
                ('numero_cuenta', models.CharField(max_length=11, unique=True)),
                ('fecha', models.CharField(max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nominas',
            fields=[
                ('cedula', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('primer_apellido', models.CharField(max_length=25)),
                ('segundo_apellido', models.CharField(max_length=25)),
                ('puesto_trabajo', models.CharField(max_length=50)),
                ('numero_cuenta', models.CharField(max_length=11, unique=True)),
                ('monto_pagar', models.FloatField(max_length=10)),
                ('empresa_rnc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.empresa')),
            ],
        ),
    ]
