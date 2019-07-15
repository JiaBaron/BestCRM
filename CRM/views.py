from django.shortcuts import render

from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    return render(request,'index.html')

@login_required
def customer_list(request):
    return render(request,'customer/customer.html')

@login_required
def base(request):
    return render(request,'base.html')

@login_required
def sell(request):
    return render(request,'sell/sell.html')