from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

def index(request):
    return render(request,'index.html',{'username':''})
    
    
def login(request):
    return render(request,'Login.html')
    
def register(request):
    return render(request,'register.html')

def logout(request):
    return redirect('/login')
