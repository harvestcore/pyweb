from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^ipcontainer', views.ipcontainer, name='ipcontainer'),
  url(r'^proyectos', views.proyectos, name='proyectos'),
  url(r'^repositorios', views.repositorios, name='repositorios'),
  url(r'^contacto', views.contacto, name='contacto'),
]