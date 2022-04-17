
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Checkerror, User
# Create your views here.
def index (request):
    return render(request,"index.html")

def addUser(request):
    errors=Checkerror.objects.validator(request.POST)
    if len(errors)  > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return 

    context = {
            'firstName' : request.POST["first_name"],
            'lastName' : request.POST["last_name"],
            'eMail' : request.POST["email"],
            'passWord' : request.POST["Password"],
            }

    request.session['firstName']=request.POST["first_name"]
    User.objects.create(first_name=context['firstName'],last_name=context['lastName'],email=context['eMail'],password=context['passWord'])
    
    return render (request,'show.html')


