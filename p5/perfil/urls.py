from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.login, name='login'),
  url(r'^$', views.logout, name='logout'),
  url(r'^$', views.signup, name='signup'),
  url(r'^$', views.profile, name='profile'),
  url(r'^$', views.modifyprofile, name='modifyprofile'),
]