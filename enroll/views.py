from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import HttpResponse
from .forms import SignUpForm,LoginForm,changepassword,EditUserProfileForm,EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login, logout,update_session_auth_hash
from django.contrib.auth.models import User
# Create your views here.

def signup(request):
  fm=SignUpForm(request.POST)
  if request.method =='POST':
   if fm.is_valid():
     messages.success(request,'Account Created Succesfully!!!')
     fm.save()
  else:
    fm=SignUpForm()
    
  return render(request,'Sign Up.html',{'form':fm})

def login(request):
 if not request.user.is_authenticated:
    if request.method =="POST":
     fm=LoginForm(request=request,data=request.POST)
     if fm.is_valid():
         uname= fm.cleaned_data['username']
         upass=fm.cleaned_data['password']
         user = authenticate(username=uname, password=upass)
         if user is not None:
            auth_login(request,user)
            messages.success(request,"Logged in Successfully!!!")
            return HttpResponseRedirect('/profile/')
         
           
         
            
         
     
    else:
       fm=LoginForm()
       
    return render(request,'login.html',{'form':fm})

 else:
     return HttpResponseRedirect('/profile/')  
     
  

def profile(request):
   if request.user.is_authenticated:
      if request.method=="POST":
         if request.user.is_superuser == True:
            fm=EditAdminProfileForm(request.POST,instance=request.user)
            users=User.objects.all()
         else:
           fm=EditUserProfileForm(request.POST,instance=request.user)
           users=None
         if fm.is_valid():
           messages.success(request,'profile Updated !!!')
           fm.save()
      else:
         if request.user.is_superuser ==True:
            fm=EditAdminProfileForm(instance=request.user)
            users= User.objects.all()
         else:
            fm=EditUserProfileForm(instance=request.user)
            users=None
      return render(request, 'Profile.html',{'name':request.user,'form':fm,'users':users})
     
   else:
      return HttpResponseRedirect('/login/')
def user_logout(request):
   logout(request)
   return HttpResponseRedirect("/login/")

def changepass(request):
 if request.user.is_authenticated:
    if request.method=='POST':
      fm=changepassword(user=request.user, data=request.POST)
      if fm.is_valid():
         fm.save()
         update_session_auth_hash(request,fm.user)
         messages.success(request,"Password changed Successfully!!!")
        
    else:
       fm=changepassword(user=request.user)
    return render(request,'changepass.html',{'form':fm})
 else:
    return HttpResponseRedirect('/login/')
def user_detail(request,id):
   if request.user.is_authenticated:
      pi=User.objects.get(pk=id)
      fm=EditAdminProfileForm(instance=pi)
      return render(request,'userdetail.html',{'form':fm})
   else:
      HttpResponseRedirect('/login/')