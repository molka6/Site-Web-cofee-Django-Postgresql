from django.shortcuts import render ,redirect
from django.contrib import messages 
from django.contrib.auth.models import User 
from .models import UserProfile
# verification E-Mail
import re 

def sign_in(request):
    if request.method== 'POST' and 'btnlogin' in request.POST : 
        inputUsername= request.POST['inputUsername']
        inputPassword= request.POST['inputPassword']
        messages.error(request, 'testing code ')
        return redirect('sign_in')

    else :    
        return render(request, 'accounts/signin.html')
 
def sign_up(request):
    if request.method== 'POST'and 'btnSignUp' in request.POST :
        fname=None 
        lname=None 
        add1=None
        add2=None
        city=None
        state=None
        zip_name=None 
        email=None 
        username=None 
        password=None
        terms=None
        # get values 
        if 'fname' in request.POST :
                   fname= request.POST['firstname']
        else: 
            messages.error(request, 'please fill in the field')
            
        if 'lname' in request.POST :
                   lname= request.POST['lastname']
        else: 
            messages.error(request, 'please fill in the field')

        if 'add1' in request.POST:
                  add1=request.POST['addr1']
        else: 
            messages.error(request, 'please fill in the field')

        if 'add2' in request.POST:
                  add2=request.POST['addr2']
        else: 
            messages.error(request, 'please fill in the field')


        if 'city' in request.POST:
                  city=request.POST['inputCity']
        else: 
            messages.error(request, 'please fill in the field')
            
        if 'zip_name' in request.POST:
                  zip_name=request.POST['inputZip']
        else: 
            messages.error(request, 'please fill in the field')


        if 'email' in request.POST:
                  email=request.POST['inputEmail']
        else: 
            messages.error(request, 'please fill in the field')


        if 'username' in request.POST:
                   username=request.POST['inputUsername']
        else: 
            messages.error(request, 'please fill in the field')


        if 'password' in request.POST:
                   password=request.POST['inputPassword']
        else: 
            messages.error(request, 'please fill in the field')


        if 'terms' in request.POST:
                   terms=request.POST['inputTerms']
        else: 
            messages.error(request, 'you agree ?')


        # if tous les champs ne sont pas vide : 
        if fname and lname and add1 and add2 and city and state and zip_name and  email and username and password : 
            if terms == 'on' :
                  

                #   verifiée que l'utlilisateur n'existe pas dans la base de donnée 
                if User.objects.filter(username= username  ).existe():
                    messages.error(request , "nom  deja existe")
                else : 
                    # l'utilisateur n'existe pas 
                    if User.objects.filter(email=  email ).existe():
                        messages.error(request , "e-mail deja utlisé")
                    else:
                        x="cjsjjkndjdd@djdfnh.mdmdld"
                        if re.match(x , email) : 
                            # ajouter 
                            user=User.objects.create_User(first_name =fname ,
                            last_name= lname ,
                             email=email ,
                             username=username ,
                             password = password)
                            user.save()

                        else:
                           messages.error(request , "e_mail invalide") 

    

                      
            else : 
                  messages.error(request, 'you agree ?')

        return redirect('index')

    else :    
          return render(request, 'accounts/signup.html')



def profile(request):
    if request.method== 'POST':
        inputUsername= request.POST['inputUsername']
        inputPassword= request.POST['inputPassword']
        messages.error(request, 'testing code ')
        return redirect('sign_up')

    else :    
        return render(request, 'accounts/profile.html') 