
from django.urls import path
from .import views
from django.contrib.auth import views as auth_view



urlpatterns = [
    path ('usuarios/', views.registrarse, name='registrarse'),
    path ('perfil/', views.perfil, name='perfil'),
    path('login/', auth_view.LoginView.as_view(template_name='usuarios/login.html'), name='usuarios-login'), 
    path('logout/', auth_view.LogoutView.as_view(template_name='usuarios/logout.html'), name='usuarios-logout'), 
     
]