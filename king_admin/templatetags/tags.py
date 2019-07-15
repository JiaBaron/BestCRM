from django import template
from django.utils.safestring import mark_safe
import datetime

register=template.Library()
@register.simple_tag
def render_app_name(admin_class):
    return admin_class.model._meta.verbose_name

@register.simple_tag
def get_query_sets(admin_class):
    return admin_class.model.objects.all()

@register.simple_tag
def build_row (obj, admin_class):
     td_ele=''
     for columns in admin_class.list_display:
         field_obj=obj._meta.get_field(columns)
         if field_obj.choices:
             columns_data=getattr(obj,'get_%s_display'%columns)()
         else:
             columns_data=getattr(obj,columns)
         td_ele+='<td>%s</td>'%columns_data
     return mark_safe(td_ele)

@register.simple_tag
def build_fliter_ele(fliter_column,admin_class):
    fliter_ele = "<select name='%s'>" % fliter_column
    column_obj = admin_class.model._meta.get_field(fliter_column)
    try:
        for choice in column_obj.get_choices():
            option = "<option value='%s'>%s</option>" % choice
            fliter_ele += option

    except AttributeError as e:
        # get_internal_type():获取字段属性
        # 因为时间的过滤方式是固定的（今天，过去七天，一个月.....），而不是从后台获取的
        if column_obj.get_internal_type() in ('DateField', 'DateTimeField'):
            time_obj = datetime.datetime.now()
            time_list = [
                ['', '--------'],
                [time_obj, 'Today'],
                [time_obj - datetime.timedelta(7), '七天内'],
                [time_obj.replace(day=1), '本月'],
                [time_obj - datetime.timedelta(90), '三个月内'],
                [time_obj.replace(month=1, day=1), 'YearToDay(YTD)'],  # 本年
                ['', 'ALL'],
            ]

            for i in time_list:
                option = "<option value='%s'>%s</option>" % (i[0], i[1])
                fliter_ele += option

    fliter_ele += "</select>"

    return mark_safe(fliter_ele)