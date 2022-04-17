from django.shortcuts import render,redirect

def index(request):
    return render(request,'index.html')

def result(request):
    if request.method == "POST":
        name=request.POST['YourName']
        location=request.POST['Dojo_Location']
        language=request.POST['Favorite_Language']
        text2=request.POST['text']
        context = {
            "name1" : name,
            "Location1" : location ,
            "Language1" : language, 
            "text2" : text2 }

        return render(request,"result.html",context)

