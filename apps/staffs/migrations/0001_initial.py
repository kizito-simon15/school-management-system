# Generated by Django 4.2.11 on 2024-04-23 14:13

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=10)),
                ('firstname', models.CharField(max_length=200)),
                ('other_name', models.CharField(blank=True, max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=10)),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now)),
                ('date_of_admission', models.DateField(default=django.utils.timezone.now)),
                ('salary', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('mobile_number', models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator(message="Entered mobile number isn't in a right format!", regex='^[0-9]{10,15}$')])),
                ('occupation', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.TextField(blank=True)),
                ('others', models.TextField(blank=True)),
            ],
        ),
    ]