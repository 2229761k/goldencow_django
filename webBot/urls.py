from django.conf.urls import include, url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.signin, name='login'),
    # url(r'^logout/$', auth_views.logout, {'next_page' : '/'}),
    url('^', include('django.contrib.auth.urls')),


]