from django.shortcuts import render,redirect

from app.models import moves

def root(request):
    return redirect ("/show")

def index(request):
    return render(request,"index.html")

def show(request):
    db=moves.objects.create(title=request.POST['titlename'],network=request.POST['networkname'],releasedate=request.POST['date'],description=request.POST['description'])
    
    return render(request,'show.html',db)
