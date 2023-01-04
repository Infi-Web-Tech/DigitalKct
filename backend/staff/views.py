from django.shortcuts import render

# Create your views here.
def dashboardPage(request):
    return render(request,'staff/dashboard.html')