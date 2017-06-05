from django.conf.urls import url

from . import views

urlpatterns = [
		url(r'^$', views.index, name='index'),


		url(r'^articulo/(?P<articulo_id>[-\w]+)/$', views.articulo, name='articulo'),

		url(r'^acerca-de/$', views.acercaDe, name='acercaDe'),
		url(r'^quienes-somos/$', views.quienesSomos, name='quienesSomos'),
		url(r'^metodologia/$', views.metodologia, name='metodologia'),
		#url(r'^distrito/(?P<distrito_nombre>[-\w]+)/$', views.distrito, name='distrito'),
		url(r'^distrito/(?P<distrito_nombre>[-\w]+)/(?P<anio>[-\w]+)/$', views.distrito2, name='distrito2'),
		#url(r'^(?P<anio>[-\w]+)/$', views.index2, name='index2'),
   

]

#handler400 = 'views.bad_request'
#handler403 = 'views.permission_denied'
#handler404 = 'views.not_found'
#handler500 = 'views.server_error' 



