from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def address(request):
    return render(request,"address.html")

def suport(request):
    return render(request,"suport.html")

def contact(request):
    return render(request,"contact.html")