from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'pages/home.html')

def aboutpage(request):
    return render(request,'pages/about.html')

def contactpage(request):
    return render(request,'pages/contact.html')

def servicespage(request):
    return render(request,'pages/services.html')

def explorepage(request):
    return render(request,'pages/explore.html')
