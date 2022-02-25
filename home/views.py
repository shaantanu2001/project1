import email
from contextlib import nullcontext
from random import random
from tempfile import tempdir

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render

from home.forms import StudentForm, Userform
from home.models import CustomUser


# Create your views here.
def home(request):
    return render(request, 'index.html')

def getrecords(request):
    temp = User.objects.all()
    return render(request, 'getusers.html', {'userslist':temp})

def deleteuser(request):
    temp = User.objects.get(id = request.GET.get('userid'))
    
    temp.delete()
    return redirect('/add')

def addstudent(request):
    if request.method == "POST":  
        form = Userform(request.POST)  
        if form.is_valid():  
            try:  
                #save the account details first
                details = form.save(commit=False)
                details.set_password(form.cleaned_data['password'])
                details.save()
                subject = 'welcome to Student registration portal world'
                message = f'Hi {details.first_name}, thank you for your patience you have been registered on the portal.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [details.email, ]
                print("hello")         
                send_mail( subject, message, email_from, recipient_list )
                return redirect('/')  
            except Exception as e: 
                return render(request, "add_student.html",{'form_name':form})
        return render(request, "add_student.html",{'form_name':form})
    else:  
        form = Userform()  
        return render(request, "add_student.html",{'form_name':form})

def update(request):
    
    if request.method == "POST":
        userid = request.POST.get("email")
        temp = User.objects.get(email = userid)  
        form = Userform(request.POST, instance = temp)  
        if form.is_valid():  
            try:  
                form.save()
            except Exception as e: 
                print(e)
            return redirect("/getstudents")
    else:
        temp = User.objects.get(id = request.GET.get('userid'))     
        form = Userform(instance = temp)
        return render(request, "update.html",{'form':form})

def login_view(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            return redirect('/')
        else:
           print(username,password)
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form, 'title':'log in'})

def logout_view(request):
    logout(request)
    return redirect('/')

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def update_new(request):
    if request.method == "POST":
        email = str(request.POST["updateEmail"])
        fname = str(request.POST["fname"])
        lname= str(request.POST["lname"])
        password =str(request.POST["password"])
        userid = str(request.POST["updateId"])
        print("hello")
        print(request.POST)
        print(userid, fname, lname, password, email)
        temp = User.objects.get(id = userid)
        temp.first_name = fname
        temp.last_name = lname
        temp.email = email
        if password != "":
            temp.set_password(password)
        temp.save()
    return HttpResponse('Updated')
