# Generated by Django 5.0.4 on 2024-04-20 01:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("corecode", "0007_alter_examtype_current"),
    ]

    operations = [
        migrations.CreateModel(
            name="Property",
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
                ("name", models.CharField(max_length=100)),
                ("quantity", models.PositiveIntegerField(default=0)),
                ("description", models.TextField(blank=True)),
                (
                    "session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="corecode.academicsession",
                    ),
                ),
            ],
        ),
    ]
