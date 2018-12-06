from django.conf.urls import url

from . import views
from .views import *

urlpatterns = [
  url(r'^login/', UserLoginView.as_view(), name='userlogin'),
  url(r'^logout/', UserLogoutView.as_view(), name='userlogout'),
  url(r'^signup/', UserSignupView.as_view(), name='usersignup'),
  
  url(r'^social/', UserConnectionsView.as_view(), name='usersocialcon'),
  
  url(r'^confirmemail/', UserConfirmEmailView.as_view(), name='confirmemail'),
  url(r'^email/', UserEmailView.as_view(), name='useremail'),
  
  url(r'^setpassword/', UserPasswordSetView.as_view(), name='setpassword'),
  url(r'^changepassword/', UserPasswordChangeView.as_view(), name='userchangepassword'),
  url(r'^resetpassword/', UserPasswordResetView.as_view(), name='resetpassword'),
]