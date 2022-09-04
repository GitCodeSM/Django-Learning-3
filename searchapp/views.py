
import email
from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from django.contrib import admin
from .models import Feature
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def homepage(request):

    features = Feature.objects.all()

    return render(request, 'index.html', {'features':features})

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Used")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Used")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')

        else:
            messages.info(request, "Password is not the same")
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')

    return render(request, 'login.html')

#for dynamic url
def page(request, pk):
    return render(request, 'page.html', {'pk':pk})

def logout(request):
    auth.logout(request)
    return redirect('/')

def counter(request):
    pages = ['Free Template', 'Template1', 'Template2', 'Template3', 'Pricing', 'Web designers', 'Back-end developers', 'Tutorials', 'Help']
    return render(request, 'counter.html', {'pages':pages})
