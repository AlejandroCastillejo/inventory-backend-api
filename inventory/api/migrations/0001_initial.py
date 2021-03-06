# Generated by Django 3.1 on 2020-08-11 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32, unique=True)),
                ('brand', models.CharField(blank=True, max_length=32)),
                ('mp_number', models.DecimalField(blank=True, decimal_places=1, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Drone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('brand', models.CharField(max_length=32)),
                ('serial_number', models.CharField(blank=True, max_length=32)),
                ('supported_cameras', models.ManyToManyField(blank=True, related_name='supported_cameras', to='api.Camera')),
            ],
        ),
    ]
