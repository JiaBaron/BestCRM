from django.contrib import admin
from CRM.models import *
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','name','qq','source','content','consultant','status','date')
    list_filter = ('source','consultant','date')
    search_fields = ('qq','name')
    raw_id_fields = ('consult_course',)
    filter_horizontal = ('tags',)
    list_editable = ('status',)
class CustomerFloowUpAdmin(admin.ModelAdmin):
    list_display = ('id','customer','content','consultant','intention','date')
class ClasslistAdmin(admin.ModelAdmin):
    list_display = ('course','branch','class_type','start_date')    #不可是多对多字段
class CourseRecordAdmin(admin.ModelAdmin):
    list_display = ('from_class','day_num','teacher','has_homework','date')

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('customer','enrolled_class','consultant','date')

class StudyRecordAdmin(admin.ModelAdmin):
    list_display = ('student','course_record','attendance','score','date')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('customer','course','consultant','amount','date')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name','user')

admin.site.register(Course)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Tag)
admin.site.register(CustomerFollowUp,CustomerFloowUpAdmin)
admin.site.register(Branch)
admin.site.register(Classlist,ClasslistAdmin)
admin.site.register(CourseRecord,CourseRecordAdmin)
admin.site.register(StudyRecord,StudyRecordAdmin)
admin.site.register(Enrollment,EnrollmentAdmin)
admin.site.register(Role)
admin.site.register(Payment,PaymentAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Menu)
