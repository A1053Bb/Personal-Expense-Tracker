from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from ExpTrack.models import *

def check(request):
    return HttpResponse("Hello, this is the testing page.\nIf you are able to see this, you have successfully loaded the repo.\nDebdeep\nSiddharthP\nSiddhartaB",content_type="text/plain")

def dashboard(request):
    return render(request,"dashboard.html")

def Login(request):
    return render(request,"index.html")

def signup(request):
    return render(request,"signup.html")

# Create your views here.

def logon1(request):
    if request.method == "POST":
        a = request.POST['email']
        b = request.POST['password']

        try:
            user = login.objects.get(emp_id=a)
            if user.pwd == b :
                request.session['username'] = user.emp_id
                return redirect('dashboard')
            else :
                messages.error(request,"Invalid password")
    
        except login.DoesNotExist :
            messages.error(request,"User does not exist")
    
    return render(request,'index.html')
