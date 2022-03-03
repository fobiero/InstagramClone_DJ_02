from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(req):
    return render(req, 'index.html')

def register(req):
    return render(req,'register.html')

def login(req):
    return render(req, 'login.html')


