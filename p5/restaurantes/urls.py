from django.conf.urls import url

from . import views
from .views import *

urlpatterns = [
  url(r'^$', RestBusquedaView.as_view(), name='restaurantes'),
  url(r'^edit/(?P<_id>[\w-]+)', RestEditView.as_view(), name='edit'),
  url(r'^delete/(?P<_id>[\w-]+)', RestDeleteView.as_view(), name='delete'),
  url(r'^add/', RestAddView.as_view(), name='add'),
]