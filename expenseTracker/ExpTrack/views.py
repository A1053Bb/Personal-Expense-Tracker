from django.shortcuts import render,redirect
from django.http import HttpResponse
from ExpTrack.models import *

def check(request):
    return HttpResponse("Hello, this is the testing page.\nIf you are able to see this, you have successfully loaded the repo.\nDebdeep\nSiddharthP\nSiddhartaB",content_type="text/plain")

def home(request):
    return render(request,"dashboard.html")

# Create your views here.

