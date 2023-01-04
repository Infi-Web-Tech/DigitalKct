from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .emailBackend import EmailBackend
# Create your views here.
def loginPage(request):
    return render(request,'authentication/login.html')

def logoutPage(request):
    return render(request,'authentication/logout.html')

def doLogin(request):
    if request.method =="POST":
        user=EmailBackend.authenticate(request,username=request.POST.get('username'),password=request.POST.get('password'),)
        print(bool(user))

        if user != None:
            login(request,user)
            user_type=user.user_types
            
            print(user_type)
            if user_type == '1':
                return redirect('hod:dashboard')
                
            if user_type == '2':
                return redirect('dashboard')
            if user_type == '3':
                pass
            else:
                messages.error(request,"Email and password are invalid")
                return redirect('login')
        else:
            messages.error(request,"User account is not valid! please sign up!!")
            return redirect('login')
    else:
        messages.error(request,"Email and password are invalid")
        return redirect('login')
        



    