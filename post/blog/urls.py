from django.urls import path
from .import views


urlpatterns =[
    path('', views.index, name='blog-index'),
    path('about/', views.about, name='blog-about'),
    path('detalle_post/<int:pk>/', views.detalle_post, name= 'detalle_post'),
    path('editar_post/<int:pk>/', views.editar_post, name= 'editar_post'),
    path('borrar_post/<int:pk>/', views.borrar_post, name= 'borrar_post'),
    

]
