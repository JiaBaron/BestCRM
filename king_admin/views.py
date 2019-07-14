from django.shortcuts import render
from king_admin import king_admin
# Create your views here.

def table(request):
    # print(king_admin.enabled_admins['CRM']['customer'].model)
    return render(request,'king_admin/table_index.html',{'table_list':king_admin.enabled_admins})
