import imp
from django import forms
from django.contrib.auth.forms import UserChangeForm,UserCreationForm,AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth.models import User
from pyexpat import model
from django.forms import fields


class Register_form(UserCreationForm):
    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={'class':'form-control','required':True}))
    first_name = forms.CharField(label="First Name",widget=forms.TextInput(attrs={'class':'form-control','required':True}))
    last_name = forms.CharField(label = "Last Name",widget=forms.TextInput(attrs={'class':'form-control','required':True}))
    email = forms.EmailField(label="Email address",widget=forms.EmailInput(attrs={'class':'form-control','required':True}))
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control','required':True}))
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':'form-control','required':True}))
    class Meta:
        model = User
        fields=['username','first_name','last_name','email']
      

class Login_form(AuthenticationForm):
    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={'class':'form-control','required':True}))
    password = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control','required':True}))
    class Meta:
        model = User
        fields = '__all__'
        