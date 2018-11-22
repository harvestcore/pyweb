from django.conf.urls import url

from . import views
from .views import *

urlpatterns = [
  url(r'^login', LoginView.as_view(), name='login'),
  url(r'^logout', LogoutView.as_view(), name='logout'),
  url(r'^signup', SignupView.as_view(), name='signup'),
  url(r'^profile', ProfileView.as_view(), name='profile'),
  url(r'^modifyprofile', UpdateProfileView.as_view(), name='modifyprofile'),
]