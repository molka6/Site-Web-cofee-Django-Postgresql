from django.shortcuts import render

# Create your views here.
def sign_in(request):
    return render(request, 'accounts/signin.html')
 
def sign_up(request):
    return render(request, 'accounts/signup.html')