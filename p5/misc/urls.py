from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.ipcontainer, name='ipcontainer'),
  url(r'^$', views.proyectos, name='proyectos'),
  url(r'^$', views.repositorios, name='repositorios'),
]