from django.shortcuts import HttpResponse,render,redirect
from file.models import Uploadfile,filesize
import base64
from django.conf import settings
from django.contrib import messages
def index(request):
    if request.method =="POST":
        title = request.POST.get('title')
        thumb = request.POST.get('image')
        Files = request.FILES['upload']
        
        print("The data is : ",title,thumb,Files)

        file   = Uploadfile.objects.create(title=title,file=Files,img=thumb)
        file.save()
        messages.add_message(request, messages.SUCCESS, 'Success! Your Files is Successfully Upload to the server')

    return render(request,'index.html',)

def Login(request):
    return render(request,"login.html")

def Download(request):
    all  = Uploadfile.objects.all()
    return render(request,"download.html",{'project':all,'list':False})

def Search(request,search):
    all  = Uploadfile.objects.all()

    searchdata = []
    for item in all :
        if search in item.title:
            searchdata.append(item)
    return render(request,"download.html",{'project':searchdata,'list':True})
