from django.conf.urls import url

from . import views
from .views import *

urlpatterns = [
  url(r'^$', RestBusquedaView.as_view(), name='restaurantes'),
  url(r'^edit/(?P<_id>[\w-]+)', RestEditView.as_view(), name='edit'),
  url(r'^delete/(?P<_id>[\w-]+)', RestDeleteView.as_view(), name='delete'),
  url(r'^add/', RestAddView.as_view(), name='add'),
  url(r'^addplato/', PlatoAddView.as_view(), name='addplato'),
  url(r'^platos/', PlatoBusquedaView.as_view(), name='platos'),
  url(r'^plato/(?P<id_>[\w-]+)', PlatoSeeView.as_view(), name='seeplato'),
  url(r'^editplato/(?P<id_>[\w-]+)', PlatoEditView.as_view(), name='editplato'),
  url(r'^deleteplato/(?P<id_>[\w-]+)', PlatoDeleteView.as_view(), name='deleteplato'),

  url(r'^r2/', RestBusqueda2View.as_view(), name='restaurantes2'),
  url(r'^intervalodatos/(?P<ini>[\w-]+)/(?P<cantidad>[\w-]+)/(?P<nombre>[\w-]+)', IntervaloView.as_view(), name='intervalo_datos'),

  url(r'^statistics/', StatisticView.as_view(), name='statistics'),
  url(r'^stat/(?P<name>[\w-]+)', views.restStat, name='stat'),
]