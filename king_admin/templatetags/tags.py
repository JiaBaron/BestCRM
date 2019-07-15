from django import template
from django.utils.safestring import mark_safe

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
