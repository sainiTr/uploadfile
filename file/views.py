from django.shortcuts import render,redirect
from file.models import Uploadfile,filesize
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
# import base64

def index(request):
    print(request.user.is_anonymous)
    if not request.user.is_anonymous:
        if request.method =="POST":
            title = request.POST.get('title')
            thumb = request.FILES["thumbnail"]
            desc = request.POST.get('desc')
            Files = request.FILES['upload']
            
            print("The data is : ",title,thumb,Files,desc)

            file   = Uploadfile.objects.create(title=title,img=thumb,file=Files,desc=desc)
            file.save()
            messages.add_message(request, messages.SUCCESS, 'Success! Your Files is Successfully Upload to the server')

        return render(request,'index.html',)
    else:
        return redirect('login')

def Login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user  = authenticate(username=username,password=password)
        print("the authentications is : ",user)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request,"login.html")

def Logout(request):
    logout(request)
    return redirect('login')

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
