from email import message
from django.dispatch import receiver
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate
from .models import Message
from django.http import HttpResponse, JsonResponse
from app.models import Message

def home(request):
    return redirect('register')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'password Already Used')
            return redirect('register')
    else:
        return render(request, 'register.html')



def login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')


def dashboard(request):
     return render(request, 'dashboard.html')


def write(request):
    return render(request, 'write.html')


def getMessagesall(request):
    messages = Message.objects.filter(read = 'True') 
    return JsonResponse({"messages": list(messages.values())})


def readall(request):
    return render(request, 'readall.html',{'typeread':"all", 'action':"dashboard"})


def getMessagesnew(request):
    messages = Message.objects.filter(read = 'False') 
    return JsonResponse({"messages": list(messages.values())})


def readnew(request):
    return render(request, 'readall.html',{'typeread':"new", 'action':"cleannew"})


def sendMessage(request):
    message = request.POST['message']
    username = request.POST['username']
    receiver = request.POST['receiver']
    subject = request.POST['subject']
    new_message = Message.objects.create(value=message, receiver=receiver, sender=username,subject=subject)
    new_message.save()
    return HttpResponse('Message sent successfully')


def deletemessage(request,user):
    print(request)
    message = request.POST['message']
    print(message)
    return render(request, 'user.html',{'username':user})
    

def cleannew(request):
    copymessages = Message.objects.filter(read = 'False') 
    for message in copymessages:
        message.read = True
        message.save()
    return redirect('/dashboard')