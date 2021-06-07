from django.http.response import HttpResponseNotModified
from django.shortcuts import render,HttpResponse

def index(request):
    context = {
        'name':"Gaurav"
    }

    if request.method == "POST":
        FileURL = request.POST.get('myfile')
        print(FileURL)
    
    return render(request,'index.html',context)
    #return HttpResponse("This is Home Page")