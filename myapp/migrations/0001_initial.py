# Generated by Django 2.2 on 2020-12-09 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='LibroEditorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.BigIntegerField()),
                ('titulo', models.CharField(max_length=80)),
                ('fecha_publicacion', models.DateField()),
                ('cantidad_paginas', models.PositiveSmallIntegerField()),
                ('edicion', models.PositiveSmallIntegerField(default=1)),
                ('idioma', models.CharField(max_length=30)),
                ('autores', models.ManyToManyField(to='myapp.Autor')),
                ('editorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Editorial')),
            ],
        ),
    ]
