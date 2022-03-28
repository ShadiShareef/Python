from django.shortcuts import render,redirect
import random

def index(request):
    if 'Ran_number' not in request.session:
        request.session['Ran_number']=random.randint(1, 100)
    return render(request,"index.html")
        

def check(request):
    if request.method == "POST": 
        if int(request.session['Ran_number']) == int(request.POST["my_number"]):
            request.session["value"]="the value is true"
            request.session['Ran_number']=random.randint(1, 100) 

        elif int(request.session['Ran_number']) > int(request.POST["my_number"]):
            request.session["value"]="you value is smaller than the namber "


        elif int(request.session['Ran_number']) < int(request.POST["my_number"]):
            request.session["value"]="you value is higher than the namber "
        
    return render(request,"index.html")