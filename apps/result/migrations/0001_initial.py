# Generated by Django 4.2.11 on 2024-04-23 13:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('corecode', '0007_alter_examtype_current'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_score', models.IntegerField(blank=True, default=None, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50)])),
                ('exam_score', models.IntegerField(blank=True, default=None, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50)])),
                ('average', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('overall_average', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('overall_status', models.CharField(default='FAIL', max_length=10)),
                ('status', models.CharField(default='FAIL', max_length=10)),
                ('gpa', models.DecimalField(decimal_places=3, default=0.0, max_digits=5)),
                ('subject_grade', models.CharField(default='F', max_length=1)),
                ('current_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corecode.studentclass')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corecode.examtype')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corecode.academicsession')),
            ],
            options={
                'ordering': ['subject'],
            },
        ),
    ]
