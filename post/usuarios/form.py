from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Perfil

class RegistroForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    

    def __init__(self, *args, **kwargs): 
        super(RegistroForm, self).__init__(*args, **kwargs)


        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class ActualizarForm(forms.ModelForm):
    class Meta:
        model = User
        fields =    ['username', 'email'] 
    
    def __init__(self, *args, **kwargs): 
        super(ActualizarForm, self).__init__(*args, **kwargs)


        for fieldname in ['username', 'email']:
            self.fields[fieldname].help_text = None


class ActualizarPerfilForm(forms.ModelForm):
    class Meta:
        model= Perfil
        fields = ['imagen']

