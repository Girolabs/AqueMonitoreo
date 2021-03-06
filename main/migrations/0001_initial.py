# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 20:08
from __future__ import unicode_literals

import ckeditor.fields
import ckeditor_uploader.fields
import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='', max_length=500, unique=True)),
                ('contenido', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='')),
                ('link', models.CharField(blank=True, help_text='Atencion, omitir los espacios en blancos y caracteres espciales, solo letras y _ y -', max_length=500, null=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')])),
            ],
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Complete con un nombre de Distrito/ciudad/Pais/Governacion. Ej: Luque', max_length=200)),
                ('descripcion', models.CharField(blank=True, max_length=300)),
                ('periodo_inicio', models.DateField(default=datetime.date(2016, 4, 20))),
                ('periodo_fin', models.DateField(default=datetime.date(2016, 4, 20))),
            ],
        ),
        migrations.CreateModel(
            name='Eje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Complete con un nombre de Eje. Ej: Educacion', max_length=200)),
                ('breve_explicacion', models.CharField(blank=True, max_length=200)),
                ('imagen', models.ImageField(upload_to=b'', verbose_name='imagen')),
                ('imagen_destacada', models.ImageField(upload_to=b'', verbose_name='Imagen Destacada')),
                ('distrito', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ejes', to='main.Distrito')),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.CharField(help_text='Escriba la pregunta o compromiso hecho al mandatario', max_length=500)),
                ('estado', models.CharField(choices=[('Sin Esdado', 'Sin Estado'), ('Aprobado', 'Aprobado'), ('No aprobado', 'No aprobado')], default='Sin Estado', max_length=15)),
                ('respuesta', ckeditor.fields.RichTextField(blank=True, default='', help_text='La respuesta es una respuesta de hasta 200 caracteres')),
                ('orden', models.IntegerField(default=1, help_text='Donde el de orden 0 aparece primero en la lista que  el orden 1')),
                ('eje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preguntas', to='main.Eje')),
            ],
            options={
                'ordering': ['orden', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=200)),
                ('descripcion', ckeditor.fields.RichTextField(blank=True, default='')),
                ('logo', models.ImageField(upload_to=b'', verbose_name='Logo')),
                ('url', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='pregunta',
            name='responsables',
            field=models.ManyToManyField(to='main.Responsable'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='preguntas',
            field=models.ManyToManyField(related_name='articulos', to='main.Pregunta'),
        ),
    ]
