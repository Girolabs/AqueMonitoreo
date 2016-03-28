# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from models import Eje, Pregunta, Distrito,Articulo
import unicodedata



def index(request):
	lista_eje = Eje.objects.all()
	lista_pregunta = Pregunta.objects.all()
	lista_distrito = Distrito.objects.all()

	distrito_principal = lista_distrito.first()


	context = {'lista_eje':lista_eje , 'lista_pregunta':lista_pregunta, 'lista_distrito':lista_distrito, 'distrito_principal':distrito_principal}
	return render_to_response('index.html', context)
# Create your views here.



def articulo(request, articulo_id):
	#serializar(articulo_id)
	articulo  = Articulo.objects.get(titulo = articulo_id.replace("_"," "))
	

	pregunta = Pregunta.objects.get(id=articulo.pregunta.id)
	context = {'articulo':articulo, 'pregunta':pregunta}
	#print pregunta.pregunta

	return render_to_response('interna.html', context)

def distrito(request, distrito_nombre):

	distrito_principal =  Distrito.objects.get(nombre = distrito_nombre.replace("_"," ")) 
	lista_eje = Eje.objects.filter(distrito = distrito_principal)
	lista_pregunta = Pregunta.objects.filter(eje__distrito = distrito_principal)
	lista_distrito = Distrito.objects.all()

	


	context = {'lista_eje':lista_eje , 'lista_pregunta':lista_pregunta, 'lista_distrito':lista_distrito, 'distrito_principal':distrito_principal}
	return render_to_response('index.html', context)



def serializar( cadena):

	aux = unicodedata.normalize('NFKD', cadena ).encode('ascii', 'ignore')
	print "serializar"
	print aux.replace(" ","_")
	return
