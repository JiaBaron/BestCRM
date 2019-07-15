
from django.conf.urls import url
from student.views import *

urlpatterns = [


    url('student/',student,name='stu_index'),#为url起了个别名，改这里的url，前端不用改变
    url('my_course/',my_course,name='my_course'),

]
