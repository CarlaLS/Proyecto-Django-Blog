from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .form import RegistroForm, ActualizarForm, ActualizarPerfilForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def registrarse(request):
    if request.method == 'POST':
       form = RegistroForm(request.POST)
       if form.is_valid():
        form.save()
        return redirect('usuarios-login')

    else:
       form= RegistroForm()    
    contexto = {
        'form': form,
    }
    return render (request, 'usuarios/registrarse.html', contexto)

@ login_required
def perfil (request):

    if request.method == 'POST':
        a_form= ActualizarForm(request.POST or None, instance=request.user)
        ap_form =ActualizarPerfilForm(request.POST or None, request.FILES or None, instance=request.user.perfil)

        if a_form.is_valid() and ap_form.is_valid():
          a_form.save()
          ap_form.save()
          return redirect('perfil')

    else: 
     a_form= ActualizarForm(instance=request.user)
     ap_form =ActualizarPerfilForm(instance=request.user.perfil)

    contexto= {
        'a_form': a_form,
        'ap_form': ap_form
    } 
    return render (request, 'usuarios/perfil.html', contexto )    