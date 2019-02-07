from django.conf.urls import include, url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.signin, name='login'),
    url(r'^logout/$', views.signout, name='signout'),
    url(r'^listingbot/$', views.listingbot, name='listingbot'),
    url(r'^apisetting/$', views.apisetting, name='apisetting'),
    url(r'^arbitragebot/$', views.arbitragebot, name='arbitragebot'),


]