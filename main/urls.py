from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    

    url(r'^articulo/(?P<articulo_id>\w+)/$', views.articulo, name='articulo'),
    url(r'^(?P<distrito_nombre>\w+)/$', views.distrito, name='articulo'),
]
