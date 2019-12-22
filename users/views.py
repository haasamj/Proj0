from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib import auth
from .models import CustomUser
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_view(request):
    if request.method=='POST':
        username = request.POST['uname']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.success(request,"username and password must be correct")
            return redirect('user:login')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        print(request.POST['telno'])
        user = CustomUser.objects.create_user(
            username=request.POST['uname'],
            email=request.POST['email'],
            password=request.POST['password'],
            full_name=request.POST['fullname'],
            phone=request.POST['telno'],
        )
        user.save()
        return redirect('user:login')
    return render(request,'signup.html')

@login_required
def logout(request):
    try:
        auth.logout(request)
    except KeyError:
        pass
    return redirect('/')
