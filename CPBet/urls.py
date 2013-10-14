__author__ = 'tippytip'
from django.conf.urls import patterns, url
from .views import login_template, register_template
from CPBet import confirm
from CPBet.authentification import login, register

urlpatterns = patterns('',
                       url(r'^$', login_template, name='login_template'),
                       url(r'^register/$', register_template, name='register_template'),
                       url(r'^login/$', login, name='login'),
                       url(r'^reg/$', register, name='register'),
                       url(r'^confirm/$', confirm, name='confirm'),
                       )