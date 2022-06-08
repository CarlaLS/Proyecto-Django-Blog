from django.contrib import admin
from .models import *



class PostAdmin(admin.ModelAdmin):
     search_fields= ['titulo']
     list_display = ('titulo', 'estado', 'fecha_creacion',)
    

admin.site.register(Post, PostAdmin),
admin.site.register(Comentario),





