from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect

def index(request):
    pass
    return render(request,"login/index.html")

def login(request):
    pass
        

    return render(request,"login/index.html")

def register(request):
    pass
    return render(request,"login/index.html")

def forgot(request):
    pass
    return render(request,"login/forgot.html")

def logout(request):
    pass
    return redirect('/index/')