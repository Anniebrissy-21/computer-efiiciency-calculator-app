# Generated by Django 5.0 on 2024-04-18 06:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_name', models.CharField(max_length=100)),
                ('machine_serial_no', models.CharField(max_length=50)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Production_log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cycle_no', models.CharField(max_length=10)),
                ('unique_id', models.CharField(max_length=100, unique=True)),
                ('material_name', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('duration', models.FloatField()),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='machine', to='api.machines')),
            ],
        ),
    ]
