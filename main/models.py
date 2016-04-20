# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

from ckeditor.fields import RichTextField

from ckeditor_uploader.fields import RichTextUploadingField
import datetime

from datetime import date
import unicodedata

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, validate_slug
from django.template.defaultfilters import slugify


# Create your models here.

class Distrito (models.Model):
	nombre =  models.CharField(max_length=200, help_text="Complete con un nombre de Distrito/ciudad/Pais/Governacion. Ej: Luque")
	descripcion = models.CharField( max_length = 300 , blank=True )
	periodo_inicio = models.DateField(default=date.today() )
	periodo_fin = models.DateField( default=date.today())
	def _get_dias_poder(self):
		"Retorna el  porcentaje de preguntas aprobadas"
		delta =   date.today() - self.periodo_inicio
		return delta.days
	dias_poder = property(_get_dias_poder)

	def _get_total_dias(self):
		"Retorna el total de dias de todo el mandato"
		delta2 =   self.periodo_fin - self.periodo_inicio
		return float(float(self.dias_poder) / float(delta2.days)) #float(self.dias_poder / delta2.days)
	porcentaje_dias = property(_get_total_dias)

	def _get_url(self):
		"Retorna la url relativo"		
		return self.nombre.replace(" ","_")

	url = property(_get_url)

	def __unicode__(self):
		return self.nombre

class Eje(models.Model):
	distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE, related_name='ejes', null=True)
	nombre = models.CharField(max_length=200, help_text="Complete con un nombre de Eje. Ej: Educacion")
	breve_explicacion = models.CharField(max_length=200 , blank=True )
	imagen = models.ImageField("Icono")
	def _get_total_aprobado(self):
		"Retorna el total de preguntas Aprobadas del eje"
		return len(Pregunta.objects.filter(eje_id=self.id, estado = "Aprobado"))
	total_aprobado = property(_get_total_aprobado)
	def _get_total(self):
		"Retorna el  total de  Preguntas del eje"
		return len(Pregunta.objects.filter(eje_id=self.id))
	total = property(_get_total)
	def _get_porcentaje(self):
		"Retorna el  porcentaje de preguntas aprobadas"
		if self.total != 0 :
			aux =   round (float( float(self.total_aprobado) / float(self.total)) * 100 , 0)
			return aux
	porcentaje = property(_get_porcentaje)
	imagen_destacada = models.ImageField("Imagen Destacada")


	


	def __unicode__(self):
		return self.distrito.nombre + "-" + self.nombre


class Responsable(models.Model):
	nombre = models.CharField(max_length=200 , blank=True )
	descripcion = RichTextField(default="", blank=True );
	logo = models.ImageField("Logo", blank=True , null=True)
	url = models.URLField( blank=True , null=True)

	def __unicode__(self):
		return  self.nombre



class Pregunta(models.Model):
	pregunta  = models.CharField(max_length=500, help_text="Escriba la pregunta o compromiso hecho al mandatario")	
	eje = models.ForeignKey(Eje, on_delete=models.CASCADE, related_name='preguntas')	
	POSIBLES_ESTADOS = (
	        ('Sin Esdado', 'Sin Estado'),
			('Aprobado', 'Logrado'),
			('No aprobado', 'No logrado'),
	)
	estado = models.CharField(max_length=15,
    						 choices=POSIBLES_ESTADOS, 
    						 default='Sin Estado')
	respuesta = RichTextField(default="", blank=True , help_text="La respuesta es una respuesta de hasta 200 caracteres");
	responsables = models.ManyToManyField(Responsable,  blank=True , null=True )
	orden = models.IntegerField(default=1,  help_text="Donde el de orden 0 aparece primero en la lista que  el orden 1")
	def __unicode__(self):
		return self.eje.nombre  + "-" + self.pregunta[:50] + "..."
	class Meta:
		ordering = ['orden','id']


class Articulo(models.Model):
	"""docstring for Articulo"""
	titulo = models.CharField(max_length=500,unique=True, default="")
	contenido = RichTextUploadingField(default="", blank=True );
	preguntas =  models.ManyToManyField(Pregunta,related_name="articulos")
		

	def _get_url(self):
		"Retorna el total de preguntas Aprobadas del eje"
		aux = unicodedata.normalize('NFKD', self.titulo ).encode('ascii', 'ignore')
		return aux.replace(" ","_")
	url = property(_get_url)
	def __unicode__(self):
		return self.titulo
	
	link = models.CharField(max_length=500,unique=False, null=True, blank=True,validators=[validate_slug],  help_text="Atencion, omitir los espacios en blancos y caracteres espciales, solo letras y _ y -")
	

	def save(self, *args, **kwargs):
        #check if the row with this hash already exists.
		
		if not self.link: 
			self.link = slugify(self.titulo) 
        
		super(Articulo, self).save(*args, **kwargs)



   