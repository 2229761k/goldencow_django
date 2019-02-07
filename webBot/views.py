from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.template import RequestContext

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            print('success')

            return redirect('login')
        else :
            return HttpResponse('failed')
    else:
        form = UserForm()
        return render(request, 'webBot/signup.html', {'form': form})

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            print('success')
            return redirect('dashboard')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'webBot/login.html', {'form': form})

def signout(request):
    logout(request)
    return render(request, 'webBot/home.html', {})

def home(request):
    return render(request, 'webBot/home.html', {})

# Create your views here.
def dashboard(request):
    return render(request, 'webBot/dashboard.html', {})

def listingbot(request):
    return render(request, 'webBot/listingbot.html', {})
