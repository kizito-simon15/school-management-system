# Generated by Django 3.2.19 on 2024-04-18 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corecode', '0004_auto_20201124_0614'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('current', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]