from django.views.generic import TemplateView
from django.shortcuts import render
from .processtable import process_table, display_table

def index(request):
    if request.method == "POST":
        file1 = request.FILES['myfile']
        a = process_table(file1)
        
        return render(request,'index.html',{'status':"Uploaded"})

def tableview(request):
    var = display_table("tabledata")