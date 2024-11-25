# Generated by Django 4.2 on 2024-11-09 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("municipio", "0001_initial"),
        ("nivelRuta", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="RutaCritica",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "codigo",
                    models.CharField(max_length=5, unique=True, verbose_name="Código"),
                ),
                (
                    "descripcion",
                    models.CharField(max_length=100, verbose_name="Descripción"),
                ),
                (
                    "municipio",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="municipio.municipio",
                        verbose_name="Municipio",
                    ),
                ),
                (
                    "nivelRuta",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="nivelRuta.nivelruta",
                        verbose_name="Nivel de Ruta",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Rutas Críticas",
            },
        ),
    ]
