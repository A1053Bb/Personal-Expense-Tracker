from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from ExpTrack.models import *

def check(request):
    return HttpResponse("Hello, this is the testing page.\nIf you are able to see this, you have successfully loaded the repo.\nDebdeep\nSiddharthP\nSiddhartaB",content_type="text/plain")

def dashboard(request):
    emp_id = request.session.get('emp_id')
    user = login.objects.get(emp_id=emp_id)
    txns = Issue.objects.filter(emp_i = user)

    return render(request,"dashboard.html",{'emp':user.emp_id,'fname':user.firstname,'lname':user.lastname,'trans':txns})

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
                request.session['emp_id'] = user.emp_id
                return redirect('dashboard')
            else :
                messages.error(request,"Invalid password")
    
        except login.DoesNotExist :
            messages.error(request,"User does not exist")
    
    return render(request,'index.html')

def su(request):
    if request.method == "POST":
        l = request.POST.get('lname')
        f = request.POST.get('fname')
        e = request.POST.get('email')
        p = request.POST.get('password')
        c = request.POST.get('confirm-password')

        if p != c :
            messages.error(request, "Passwords do not match.")
            return redirect('signup')
        
        try :
            user = login(firstname = f, lastname = l, emp_id = e, pwd = p)
            user.save()
            messages.success(request, "Sign-Up Successful!")
            return redirect('login')
        
        except Exception as e :
            messages.error(request, f"Error: {str(e)}")
            return redirect("signup")
    else :
        return render(request, "signup.html")

def logout(request):
    request.session.flush()
    return redirect('login')

def income_expense_api(request,emp_id):
    income = Issue.objects.filter(emp_i = emp_id, txn_type = "Credited").aggregate(total_income = models.Sum('charges'))['total_income'] or 10
    expenditure = Issue.objects.filter(emp_i = emp_id, txn_type = "Debited").aggregate(total_expenditure = models.Sum('charges'))['total_expenditure'] or 20
    # print("Income:", income, "Expenditure:", expenditure)
    return JsonResponse({'income':income, 'expenditure':expenditure})