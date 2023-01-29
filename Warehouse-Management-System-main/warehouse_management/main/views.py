from django.shortcuts import render , redirect, HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import stock, sq
from django.db.models import Sum
import sqlite3
import random
import pandas as pd


def home(request):
    return render(request,'main/index.html')

def entry(request):
    return render(request,'main/entry.html')
def report(request):
    return render(request,'main/report.html')

def createuser(request):
    return render(request,'main/createuser.html')

def admin(request):
    stocks = sq.objects.all()
    # sname=request.get['s_name']
    # print(stocks)
    
    quantities=sq.objects.values('s_name').annotate(quantity=Sum('s_in')-Sum('s_out'))
    for quantity in quantities:
        s_name = quantity['s_name']
        tq = quantity['quantity']
        print(s_name,tq )
    return render(request,'main/admin.html',{'stocks': stocks, 'quantities':quantities} )

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username=username, password=pass1)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Logged In Sucessfully!!")
            return redirect('home')
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')
    return render(request, 'main/loginpage.html')

# def map(request):
#     return render(request, 'main/map.html')


def dbtest(request):
    connection = sqlite3.connect("db.sqlite3")
    crsr = connection.cursor()

    for i in range(0,100):
        randnum = random.randrange(200, 400)
        crsr.execute('INSERT INTO main_prophet VALUES ({i}, "Sting", "2023-01-24" , 600)')

    # crsr.execute(sql_command)
    connection.commit()
    connection.close()
    return render(request, 'main/index.html')


def stock_chart_view(request):
    stocks = sq.objects.all()
    print(stocks)
    return render(request, 'main/admin.html', {'stocks': stocks})

def prophet(request):
    
    
    return HttpResponse("masti")



