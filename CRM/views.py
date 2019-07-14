from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request,'index.html')


def customer_list(request):
    return render(request,'customer/customer.html')

def base(request):
    return render(request,'base.html')

def sell(request):
    return render(request,'sell/sell.html')