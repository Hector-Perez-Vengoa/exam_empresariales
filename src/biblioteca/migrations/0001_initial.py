# Generated by Django 5.2 on 2025-04-09 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=100)),
                ('anio', models.PositiveIntegerField()),
                ('categoria', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=13)),
                ('descripcion', models.TextField(blank=True)),
                ('puntuacion', models.DecimalField(decimal_places=1, default=0.0, max_digits=2)),
            ],
        ),
    ]
