from django.conf.urls import url

from . import views
from .views import *

urlpatterns = [
  url(r'^$', RestBusquedaView.as_view(), name='restaurantes'),
]