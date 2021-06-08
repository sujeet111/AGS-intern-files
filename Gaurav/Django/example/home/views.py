from django.shortcuts import render,HttpResponse
from .models import FileUpload
from .logic import executefile, getdata

def index(request):
    context = {
        'name':"Gaurav",
        'status':"Not Uploaded"
    }
    if request.method == "POST":
        file1 = request.FILES['myfile']
        document = FileUpload.objects.create(file = file1)
        document.save()
        a = executefile(file1)
        #return HttpResponse("Your file was uploaded with code : "+str(a))
        return render(request,'index.html',{'name':"Gaurav",'status':"Uploaded"})

    return render(request,'index.html',context)
    #return HttpResponse("This is Home Page")

    # create superuser

def show(request):
    a = getdata("Table_1")
    return render(request,'table.html',{'table':a,'Name':"Table 1"})

def show2(request):
    a = getdata("Table_2")
    return render(request,'table.html',{'table':a,'Name':"Table 2"})

def show3(request):
    a = getdata("Table_3")
    return render(request,'table.html',{'table':a,'Name':"Table 3"})