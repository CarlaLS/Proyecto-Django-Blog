from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.





class Post (models.Model):
    id= models.AutoField(primary_key=True)
    estado=models.BooleanField('Estado', default=True)
    fecha_creacion=models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)
    titulo=models.CharField('Titulo', max_length=150, unique=True)
    subtitulo=models.CharField('Subtitulo',  unique= True,  max_length=250)
    autor= models.ForeignKey(User, on_delete=models.CASCADE)
    contenido= RichTextField()
    imagen = models.URLField( blank=False, null=False)
    
    
    

    class Meta:
        verbose_name='Post'
        verbose_name_plural= 'Posts'
        ordering = ('-fecha_creacion',)

    def  comentario_count(self):
         return self.comentario_set.all().count()

    def comentarios(self):
        return self.comentario_set.all()    

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    usuario= models.ForeignKey(User, on_delete=models.CASCADE)
    post= models.ForeignKey(Post, on_delete=models.CASCADE)
    contenido= models.CharField(max_length=300)


    def __str__(self):
        return self.contenido
