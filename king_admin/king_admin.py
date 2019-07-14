from django.contrib import admin
from CRM.models import *

# Register your models here.

enabled_admins={}

class BaseAdmin(object):
    list_display=[]
    list_fliter=[]

class CustomerAdmin(BaseAdmin):
    list_display = ['qq','name']

class CustomerFollowUpAdmin(BaseAdmin):
    list_display = ['customer','consultant']


def register(model_class,admin_class=None):
    if model_class._meta.app_label not in enabled_admins:
        enabled_admins[model_class._meta.app_label]={}

    admin_class.model=model_class   #绑定model对象和admin类
    enabled_admins[model_class._meta.app_label][model_class._meta.model_name]=admin_class


register(Customer,CustomerAdmin)
register(CustomerFollowUp,CustomerFollowUpAdmin)