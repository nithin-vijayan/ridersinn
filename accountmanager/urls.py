from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from . import views

#app_name='accountmanager'

urlpatterns = [

    url(r'^signup/', views.userSignup, name="signup"),
    url(r'^login/', auth_views.login , {'template_name': 'accountmanager/login.html'}, name="login"),
    url(r'^logout/', auth_views.logout, {'next_page':'login'} , name="logout"),
    url(r'^change/', views.changePassword, name="change"),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),

]
