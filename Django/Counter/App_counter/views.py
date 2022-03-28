# Create your views here.
from django.shortcuts import render, HttpResponse,redirect

def first_time(request):
    request.session['time']=0
    return redirect('/show')

def index(request):

    request.session['time']+=1
    return render(request,"index.html")


