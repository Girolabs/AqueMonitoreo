from django.contrib import admin

# Register your models here.




from .models import Eje,Pregunta, Articulo, Distrito, Responsable


class ArticuloAdmin(admin.ModelAdmin):
	list_display = ('titulo')


class PreguntaAdmin(admin.ModelAdmin):
	list_display = ('pregunta', 'eje', 'estado')


class EjeAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'distrito',)



admin.site.register(Distrito)
admin.site.register(Eje, EjeAdmin)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Articulo)
admin.site.register(Responsable)