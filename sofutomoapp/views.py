from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import GuestModel, HostModel, ImageModel, GoodModel
from django.views.generic import CreateView
from .forms import ImageForm, RegisterForm, HostForm
import requests
import json
import http.client
import base64
import time
import hmac
import hashlib
from django.core.mail import send_mail
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
import joblib
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.urls import reverse

def signupview(request):
    if request.method=='POST':
        username_data=request.POST['username_data']
        password_data=request.POST['password_data']
        try:
            User.objects.create_user(username_data,'',password_data)
            user=authenticate(request,username=username_data,password=password_data)
            login(request,user)
            return redirect('register')
        except IntegrityError:
            return render(request, 'signup.html', {'error':'このユーザーは既に登録されています。'})
    else:
        return render(request, 'signup.html')

"""@login_required
def registerview(request):
    
    if request.method=='POST':
        form=RegisterForm(request.POST, request.FILES)
        model=GuestModel()
        model.user = request.user
        model.name=request.user.username
        model.age = request.POST['age']
        model.gender = request.POST['gender']
        model.image = request.FILES['image']
        model.email = request.POST['email']
        print(request.POST['image'])
        model.save()
        return redirect('index')
    else:
        form=RegisterForm()
        return render(request, 'register.html', {'form':form})
"""


def registerview(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user=request.user
            name=request.user.username
            email=form.cleaned_data['email']
            gender=form.cleaned_data['gender']
            age=form.cleaned_data['age']
            #image=form.cleaned_data['image']
            obj=GuestModel.objects.create(user=user, name=name, email=email, gender=gender, age=age)
            obj.save()
            return redirect('index')
    else:
        form = RegisterForm()
    context = {'form':form}
    return render(request, 'register.html', context)

def imageview(request):
    if request.method == 'POST':
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            image=form.cleaned_data['image']
            obj=ImageModel.objects.create(image=image)
            obj.save()
            return redirect('index')
    else:
        form=ImageForm()
    context={'form':form}
    return render(request, 'register.html', context)

def loginview(request):
    if request.method=='POST':
        username_data=request.POST['username_data']
        password_data=request.POST['password_data']
        user=authenticate(request,username=username_data,password=password_data)
        if user is not None:
            login(request,user)
            print(request.user.username)
            return redirect('index')
        else:
            return redirect('login')
        
    return render(request,'login.html')





@login_required
def indexview(request):
    if request.method == 'POST':
        location=request.POST['filter']
        host_filter = HostModel.objects.filter(location = location)
        return render(request, 'index.html', {'host_list':host_filter})
    else:
        host_list=HostModel.objects.all()
        return render(request, 'index.html', {'host_list':host_list})



    
@login_required
def detailview(request, pk):
    obj=HostModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object':obj})

@login_required
def mypageview(request):
    data=GuestModel.objects.get(user=request.user)
    return render(request, 'mypage.html', {'data':data})


def evaluationview(request, pk):
    host=HostModel.objects.get(pk=pk)
    guest=GuestModel.objects.get(user=request.user)

    if host.good_counts==0:
        host.good_counts=host.good_counts + 1
        host.save()
        g=GoodModel()
        g.good_user=request.user.username
        g.gender=guest.gender
        #g.image=guest.image
        g.age=guest.age
        g.email=guest.email
        g.user=host.user
        g.save()
        return redirect('index')
    
    elif host.good_counts>0:
        for i in GoodModel.objects.all():
            if i.good_user==request.user.username:
                return redirect('index')
                break
        else:
            host.good_counts=host.good_counts + 1
            host.save()
            g=GoodModel()
            g.good_user=request.user.username
            g.gender=guest.gender
            #g.image=guest.image
            g.age=guest.age
            g.email=guest.email
            g.user=host.user
            g.save()
            return redirect('index')

def checkview(request):
    a=HostModel.objects.get(user=request.user)
    good_list=GoodModel.objects.filter(user=request.user)

    params={
        'good_list':good_list,
    }
        
    return render(request, 'good_user.html', params)    

@login_required
def hostview(request):
    h_form=HostForm()
    if request.method=='POST':
        try:
            guest=GuestModel.objects.get(user=request.user)
            host=HostModel()
            #user_dataの引継ぎ
            host.user=guest.user
            host.name=guest.name
            host.gender=guest.gender
            #host.image=guest.image
            host.age=guest.age
            host.email=guest.email
            #イベント情報
            host.location = request.POST['location']
            host.member = request.POST['member']
            host.event_date = request.POST['event_date']
            host.event_time = request.POST['event_time']
            host.save()
            return redirect('index')
        except ObjectDoesNotExist:
            return redirect('host')
    else:
        data = joblib.load( "osaka.txt")
        key_list = list(data.keys())
        return render(request, 'host.html', {'h_form':h_form, 'item': json.dumps(data), 'key_list': key_list})