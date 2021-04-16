from django.shortcuts import render

# Create your views here.

def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})

def index(request):
    return render(request, 'pages/index.html')

def About(request):
    return render(request, 'pages/about.html')



