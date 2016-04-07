# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from django.http import HttpResponse,Http404
from django.template import RequestContext

from models import Eje, Pregunta, Distrito,Articulo
import unicodedata



def index(request):
	lista_eje = Eje.objects.all()
	lista_pregunta = Pregunta.objects.all().order_by('orden')
	lista_distrito = Distrito.objects.all()

	distrito_principal = lista_distrito.first()


	context = {'lista_eje':lista_eje , 'lista_pregunta':lista_pregunta, 'lista_distrito':lista_distrito, 'distrito_principal':distrito_principal}
	return render_to_response('index.html', context)
# Create your views here.



def articulo(request, articulo_id):
	#serializar(articulo_id)
	try:
		articulo  = Articulo.objects.get(link = articulo_id)
	except Articulo.DoesNotExist:
		raise Http404("Question does not exist")
	
	
	pregunta_aux = articulo.preguntas.get();
	pregunta = Pregunta.objects.get(id=pregunta_aux.id)
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






def bad_request(request):
	response = render_to_response('400.html',context_instance=RequestContext(request))
	response.status_code = 400
	return response


def server_error(request):
	response = render_to_response('400.html',context_instance=RequestContext(request))
	response.status_code = 400
	return response