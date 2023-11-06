from django.shortcuts import render

def home(request):
    return render(request,'crm/dashbord.html')

def products(request):
    return render(request,'crm/products.html')

def customers(request):
    return render(request,'crm/customer.html')
