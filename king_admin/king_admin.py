from django.contrib import admin
from CRM.models import *         #从App CRM中导入所有的表

# Register your models here.

enabled_admins={}                #创建一个全局空字典，将用于存放App及其对象
#{'CRM': {'customer': <class 'king_admin.king_admin.CustomerAdmin'>, 'customerfollowup': <class 'king_admin.king_admin.CustomerFollowUpAdmin'>}}
class BaseAdmin(object):                 #基类      仿写Admin中自定义格式
    list_display=[]
    list_fliter=[]

class CustomerAdmin(BaseAdmin):
    list_display = ['name','qq','source','status','date']
    list_fliter = ['source']

class CustomerFollowUpAdmin(BaseAdmin):
    list_display = ['customer','consultant']


def register(model_class,admin_class=None):
    if model_class._meta.app_label not in enabled_admins:
        enabled_admins[model_class._meta.app_label]={}   #等价于 enabled_admins['CRM']={}

    admin_class.model=model_class   #绑定model对象和admin类
    enabled_admins[model_class._meta.app_label][model_class._meta.model_name]=admin_class
        ##enabled_admins['CRM']['CustomerFollowUp']=CustomerFollowUpAdmin

register(Customer,CustomerAdmin)
register(CustomerFollowUp,CustomerFollowUpAdmin)