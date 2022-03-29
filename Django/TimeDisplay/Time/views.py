from django.shortcuts import render
from datetime import datetime
    
def time_display(request):
    TimeNow = datetime.today()

    context = {
        "date": TimeNow.strftime('%b %d , %Y'), 

        "time": TimeNow.strftime('%H:%M %p') 
    }
    return render(request,'index.html', context)