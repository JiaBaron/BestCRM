
from django.conf.urls import url

from CRM.views import *
urlpatterns = [

    url('^customer_list/$',customer_list,name='customer_list'),
    url('^base/$', base),
    url('sell',sell,name='sell_index')
]
