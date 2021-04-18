from django.shortcuts import get_object_or_404 , render
from datetime import datetime
from .models import Product

def products(request):
    pro=Product.objects.all() 
    name=None
    if 'search_name' in request.GET:
        name= request.GET['serach_name']
        molka="h"
        if name: 
            pro =pro.filter(name__icontains=name)

    context ={
         'products': pro 
    }
    return render(request, 'products/products.html', context)

def product(request ,pro_id):
    context={
        'products': get_object_or_404(Product ,  pk=pro_id)
    }
    return render(request, 'products/product.html' , context)  



def search(request):
    return render(request, 'products/search.html')