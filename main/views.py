import re
from django.shortcuts import render,HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib import messages
from main.models import Contact, u_log, u_sign
from main.forms import Login_form,Register_form
from django.contrib.auth import authenticate,update_session_auth_hash,login,logout
# Create your views here.
def index(request):
    fm1 = Login_form()
    fm2 = Register_form()
    return render(request,'main/index.html',{'form1':fm1, 'form2':fm2})

def u_login(request):
    print("abcdef")
    if request.method=="POST":
        fm = Login_form(request=request,data = request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['username']
            pwd = fm.cleaned_data['password']
            print("Name",nm)
            print("Password: ",pwd)
            user = authenticate(username=nm, password=pwd)
            if user is not None:
                login(request, user)
                messages.success("Login Successfull!!!!")
                return HttpResponseRedirect('/index/')
    else:
        fm = Login_form()

    return render(request,'main/index.html',{'form1':fm})

def u_signup(request):
    print("abc")
    if request.method=="POST":
        fm = Register_form(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['username']
            pwd = fm.cleaned_data['password1']
            print("Name",nm)
            print("Password: ",pwd)
            fm.save()
            messages.success("Registeration Successfull!!!")
            return HttpResponseRedirect('/index/')
            
    else:
        fm = Register_form()
    return render(request,'main/index.html',{'form2':fm})


def contact(request):
    if request.method=="POST":
        nm = request.POST.get('name')
        em = request.POST.get('email')
        pn = request.POST.get('contact')
        mg = request.POST.get('message')
        sb = request.POST.get('subject')
        obj = Contact(name=nm, email=em, contact=pn, desc=mg, sub = sb)
        obj.save()
        str = 'You have recieved a new request Its details are: \n Name of person: ' +nm+'\n Email Id of person: '+em+'\n Contact No. of Person: '+pn+'\n Message: '+mg +'\n Suggestion:' + sb
        ob = send_mail('New Query/Suggestion',str,'arshita2523@gmail.com',['arshita2523@gmail.com','arshitkaur48@gmail.com'],fail_silently=False)
        messages.success(request,"We have recieved your Request! Our Team will get back to you soon!")
    return render(request,'main/Contact.html')

def about(request):
    return render(request,'main/About.html')

def team(request):
    return render(request,'main/team.html')
