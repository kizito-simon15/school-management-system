# Generated by Django 3.2.19 on 2024-04-18 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corecode', '0006_alter_examtype_current'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examtype',
            name='current',
            field=models.BooleanField(default=True),
        ),
    ]
