from django.shortcuts import render,HttpResponse
import random

# Create your views here.
def index(request):
    if 'Gold' not in request.session:
        request.session['Gold']=0
    return render(request,"index.html")

def get_gold(request):
    if request.POST['which_form'] == 'Farm': 
        request.session['Gold']+=random.randint(10,20) 

    elif request.POST['which_form'] == 'Cave': 
        request.session['Gold']+=random.randint(5,10) 

    elif request.POST['which_form'] == 'House': 
        request.session['Gold']+=random.randint(2,5) 

    elif request.POST['which_form'] == 'Casino': 
        request.session['Gold']-=random.randint(0,50) 

    return render(request,"index.html")
