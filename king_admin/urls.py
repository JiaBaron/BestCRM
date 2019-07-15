
from django.conf.urls import url

from king_admin.views import *
urlpatterns = [


    url('table_index/',table,name='table_index'),
    url(r'(\w+)/(\w+)/',table_objs,name='table_objs'),
    url('login/',css_login,name='login'),
    url('logout/',css_logout,name='logout'),
]
