# Generated by Django 4.2.2 on 2023-06-13 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=30)),
                ('Apellido_paterno', models.CharField(max_length=30)),
                ('Apellido_materno', models.CharField(max_length=30)),
                ('Hobbie', models.CharField(blank=True, max_length=60, null=True)),
                ('Documento', models.CharField(blank=True, max_length=60, null=True)),
                ('Tipo_documento', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
