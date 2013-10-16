from django.views.generic import DetailView
from CPBet.models import bookmaker

__author__ = 'tippytip'
from CPBet.authentification import login_method, register_method
from django.conf.urls import patterns, url
from .views import login_template, register_template
from CPBet.confirm_page import confirm


urlpatterns = patterns('',
                       url(r'^$', login_template, name='login_template'),
                       url(r'^register/$', register_template, name='register_template'),
                       url(r'^login/$', login_method, name='login'),
                       url(r'^reg/$', register_method, name='register'),
                       url(r'^confirm/$', confirm, name='confirm'),
                    # template name is defaulted to xxx_detail
                       url(r'^(?P<pk>\d+)/detail/$', DetailView.as_view(
                           context_object_name="bookmakers",
                           model=bookmaker,
                       ), name='detail'),

                       )