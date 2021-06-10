from django.views.generic import TemplateView
from django.shortcuts import render

def index(request):
    if request.method == "POST":
        file1 = request.FILES['myfile']
        document = FileUpload.objects.create(file = file1)
        document.save()
        a = executefile(file1)
        #return HttpResponse("Your file was uploaded with code : "+str(a))
        return render(request,'index.html',{'name':"Gaurav",'status':"Uploaded"})