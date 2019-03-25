from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.template import RequestContext
import sys
sys.path.append('../')
from webBot.static.fusionchart.fusioncharts import FusionCharts
import requests
from .models import Post
from django.utils import timezone

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

# 상장거래봇
def listingbot(request):
    return render(request, 'webBot/listingbot.html', {})

# api 설정
def apisetting(request):
    return render(request, 'webBot/apisetting.html', {})

# 차익거래봇
def arbitragebot(request):
    return render(request, 'webBot/arbitragebot.html', {})

# # 매집증후 포착 봇
# def zombiecowbot(request):
#     return render(request, 'webBot/zombiecowbot.html', {})

# 업비트 공지 봇
def upbitEventbot(request):
    return render(request, 'webBot/upbitEventbot.html', {})




def chart1(request):
  

    res = requests.post('http://localhost:3000/testing',  json={"symbol": 'BTC'})
    # Create an object for the column2d chart using the FusionCharts class constructor
    column2d = FusionCharts("column2d", "ex1" , "600", "400", "chart-1", "json",
         # The data is passed as a string in the `dataSource` as parameter.
        """{  
               "chart": {  
                  "caption":"Harry\'s SuperMart",
                  "subCaption":"Top 5 stores in last month by revenue",
                  "numberPrefix":"$",
                  "theme":"ocean"
               },
               "data": [  
                    {"label":"Bakersfield Central", "value":"880000"},
                    {"label":"Garden Groove harbour", "value":"730000"},
                    {"label":"Los Angeles Topanga", "value":"590000"},
                    {"label":"Compton-Rancho Dom", "value":"520000"},
                    {"label":"Daly City Serramonte", "value":"330000"}
                ]
            }""")

    # returning complete JavaScript and HTML code, 
    # which is used to generate chart in the browsers.
    column3d = FusionCharts("column2d", "ex2" , "600", "400", "chart-2", "json", 
        # The data is passed as a string in the `dataSource` as parameter.
        """{  
               "chart": {  
                  "caption":"Harry\'s SuperMart",
                  "subCaption":"Top 5 stores in last month by revenue",
                  "numberPrefix":"$",
                  "theme":"ocean"
               },
               "data": [  
                    {"label":"Bakersfield Central", "value":"880000"},
                    {"label":"Garden Groove harbour", "value":"730000"},
                    {"label":"Los Angeles Topanga", "value":"590000"},
                    {"label":"Compton-Rancho Dom", "value":"520000"},
                    {"label":"Daly City Serramonte", "value":"330000"}
                ]
            }""")
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers. 
    return  render(request, 'webBot/zombiecowbot.html', {'output1' : column2d.render(), 'output2' : column3d.render(), 'post':posts})