
from django.conf.urls import url

from king_admin.views import *
urlpatterns = [


    url('table_index/',table,name='table_index')
]
