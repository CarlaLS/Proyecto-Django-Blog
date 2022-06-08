from django import forms
from .models import Post, Comentario



class PostForm(forms.ModelForm):
    contenido = forms.CharField(widget=forms.Textarea(attrs={'rows':4}))
    
    class Meta:

        model=Post
        fields=('titulo', 'subtitulo', 'contenido', 'imagen',)


class ActualizarForm (forms.ModelForm):
    class Meta:
        model= Post
        fields= ('titulo', 'subtitulo', 'contenido', 'imagen',)



class ComentarioForm(forms.ModelForm):
    contenido = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Agrega un comentario aquí..'}))
    class Meta:
        model = Comentario
        fields = ('contenido', )
