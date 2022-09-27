from django.shortcuts import HttpResponse,render,redirect
from file.models import Uploadfile,filesize
import base64

def index(request):
    if request.method =="POST":
        title = request.POST.get('title')
        Files = request.FILES['upload']
        
        data = filesize(Files)
        # print("The File Size is : ",data)
        file   = Uploadfile.objects.create(title=title,file=Files)
        file.save()
        
            

    return render(request,'index.html')

def Login(request):
    return render(request,"login.html")

def Download(request):
    return render(request,"download.html")