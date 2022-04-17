from unicodedata import name
from django.shortcuts import render, HttpResponse,redirect
from .models import Dojo, Ninja


def index(request):
    alldojo=Dojo.objects.all()
    allninja=Ninja.objects.all()
    context={
        'alldojo':alldojo ,
        'allninja': allninja
    }
    return render(request,"index.html",context)

def addDojo(request):

    dojoname=request.POST['name']
    dojocity=request.POST['city']
    dojostate=request.POST['state']
    Dojo.objects.create(name=dojoname,city=dojocity , state = dojostate)
    return redirect('/')

def addNinja(request):

    ninja_firstName=request.POST['firstName']
    ninja_lastName=request.POST['lastName']
    selectDojo=int(request.POST['dojo'])
    ninja_dojo=Dojo.objects.get(id=selectDojo)
    Ninja.objects.create(firstName=ninja_firstName,lastName=ninja_lastName ,dojo = ninja_dojo)

    return redirect('/')