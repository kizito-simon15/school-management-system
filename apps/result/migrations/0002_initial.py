# Generated by Django 4.2.11 on 2024-04-23 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('result', '0001_initial'),
        ('students', '0001_initial'),
        ('corecode', '0007_alter_examtype_current'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student'),
        ),
        migrations.AddField(
            model_name='result',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corecode.subject'),
        ),
        migrations.AddField(
            model_name='result',
            name='term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corecode.academicterm'),
        ),
    ]
