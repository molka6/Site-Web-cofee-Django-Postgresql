from django.shortcuts import get_object_or_404 , render
from datetime import datetime
from .models import Product

def products(request):
    pro=Product.objects.all() 
    name=None
    desc=None
    pricemin=None
    pricemax=None

    
    if request.method=='GET' and 'serachname' in request.GET:
          name= request.GET['serachname']
          if name: 
                pro =pro.filter(name__icontains=name)

    if request.method=='GET' and 'serach_desc' in request.GET:
          desc= request.GET['serach_desc']
          if desc: 
                pro =pro.filter(description__icontains=desc)

    if request.method=='GET' and 'serach_price_min' in request.GET and 'serach_price_max' in request.GET:
          pricemin= request.GET['serach_price_min']
          pricemax= request.GET['serach_price_max']
          if pricemin and pricemax: 
              if pricemin.isdigit() and pricemax.isdigit(): 
                 pro =pro.filter(price__gte= pricemin ,price__lte= pricemax )
    context ={
         'products':pro   
    }
    return render(request, 'products/products.html', context)

def product(request ,pro_id):
    context={
        'products': get_object_or_404(Product ,  pk=pro_id)
    }
    return render(request, 'products/product.html' , context)  



def search(request):
    return render(request, 'products/search.html')