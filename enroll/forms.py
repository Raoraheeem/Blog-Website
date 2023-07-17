from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm,UserChangeForm


class SignUpForm(UserCreationForm):
  password2=forms.CharField(label='Confirm Password (again)',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))
  password1=forms.CharField(label='Password',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'password'}))
  username= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
  first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'first name'}))
  last_name= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'last name'}))
  email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
  class Meta:
    model=User
    fields=['username','first_name','last_name','email']
    labels={'email':'Email'}
    
    
class LoginForm(AuthenticationForm):
   username= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
   password= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'password'}))
class changepassword(PasswordChangeForm):
      old_password=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'old Password'}))
      new_password1=forms.CharField(label='New password ',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'New password'}))
      new_password2=forms.CharField(label='Confirm Password (again)',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))

class EditUserProfileForm(UserChangeForm):
    password=None
    username= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
    password= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'password'}))
    first_name= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First name'}))
    last_name= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last name'}))
    email= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    date_joined= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Date of joined'}))
    last_login=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'last login'}))
    class Meta:
     model= User
     fields=['username','first_name','last_name','email','date_joined','last_login']
     labels={'email':'Email'}

class EditAdminProfileForm(UserChangeForm):
    password=None
    username= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
    password= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'password'}))
    first_name= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First name'}))
    last_name= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last name'}))
    email= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    date_joined= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Date of joined'}))
    last_login=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'last login'}))
   
    class Meta:
     model= User
     fields= '__all__'
     labels={'email':'Email'}
  
    