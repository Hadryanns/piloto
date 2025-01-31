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

def viewitem(request,id):
    return render(request,'viewitem.html',{'id':id})

def user(request, user):
    return render(request,'userPerfil.html',{'user':user})

def weekday(request,weekday):
    week = ['Domingo','Segunda-Feira','Terça-feira','Quarta-feira','Quinta-feira','Sexta-feira','Sábado']
    if weekday < 1 or weekday > 7:
        mensagem = "Digite um valor válido"
    else:
        mensagem = f"O dia da semana é {week[weekday-1]}"
    return render(request,'weekday.html',{'msg':mensagem})