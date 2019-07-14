from django.contrib import admin
from CRM.models import *
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','name','qq','source','content','consultant','date')
    list_filter = ('source','consultant','date')
    search_fields = ('qq','name')
    raw_id_fields = ('consult_course',)
    filter_horizontal = ('tags',)
    # list_editable = ('memo',)
class CustomerFloowUpAdmin(admin.ModelAdmin):
    list_display = ('id','customer','content','consultant','intention','date')

admin.site.register(Course)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Tag)
admin.site.register(CustomerFollowUp,CustomerFloowUpAdmin)
admin.site.register(Branch)
admin.site.register(Classlist)
admin.site.register(CourseRecord)
admin.site.register(StudyRecord)
admin.site.register(Enrollment)
admin.site.register(Role)
admin.site.register(Payment)
admin.site.register(UserProfile)
admin.site.register(Menu)