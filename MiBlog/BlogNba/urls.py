from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), # Inicio
    path('post/<int:pk>/', views.post_detail, name='post_detail'), # Detalle
    path('post/new', views.post_new, name='post_new'), # Alta Post
    path('equipo/new', views.equipo_new, name='equipo_new'), # Alta Equipo
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'), # Editar Post
    path('borrador/', views.post_borrador_list, name='post_borrador_list'), # borradores
    path('post/<pk>/publicar/', views.post_publicar, name='post_publicar'), # Publicar
    path('post/<pk>/remove/', views.post_remove, name='post_remove'), # Borrar
    path('registro/', views.registro, name = 'registro'), # Registrar Usuario
    path('contacto/', views.contacto, name = 'contacto'), # Contacto
    path('Error/', views.Error, name = 'Error'), # Error
    path('about/', views.About, name = 'About'), # About

]