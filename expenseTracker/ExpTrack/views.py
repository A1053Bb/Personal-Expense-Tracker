from django.shortcuts import render
from django.http import HttpResponse

def check(request):
    return HttpResponse("Hello, this is the testing page.\nIf you are able to see this, you have successfully loaded the repo.\nDebdeep\nSiddharthP",content_type="text/plain")

# Create your views here.

