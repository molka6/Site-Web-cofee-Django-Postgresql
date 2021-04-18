from django.shortcuts import render
from datetime import datetime
# Create your views here.
from products.models import Product


def date_actuelle(request):
    
    return render(request, 'blog/date.html', {'date': datetime.now()})

def index(request):
    context={
        'products': Product.objects.all()
    }
    return render(request, 'pages/index.html' , context)

def About(request):
    return render(request, 'pages/about.html')



