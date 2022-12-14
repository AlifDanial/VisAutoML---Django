# Generated by Django 4.0.3 on 2022-11-01 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=100)),
                ('model_type', models.CharField(choices=[('RG', 'Regression'), ('CL', 'Classification')], max_length=2)),
                ('algorithm_name', models.CharField(blank=True, max_length=100, null=True)),
                ('overall_score', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('data_set', models.FileField(upload_to='datasets/')),
            ],
        ),
    ]
