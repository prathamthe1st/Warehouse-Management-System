from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import stock, sq
from django.db.models import Sum


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
    records = stock.objects.all()
    print(records)
    return render(request, 'main/index.html')

'''this was using chartit'''
# def stock_chart_view(request):
#     # Step 1: Create a DataPool with the data we want to retrieve.
#     stock_data = DataPool(
#         series=[{'options': {
#             'source': sq.objects.all()},
#             'terms': [
#                 'stock',
#                 'quantity']}
#         ])
     
#     cht = Chart(
#         datasource=stock_data,
#         series_options=[{'options':{
#             'type': 'column',
#             'stacking': False},
#             'terms':{
#                 'stock': [
#                     'quantity']
#                 }
#             }],
#         chart_options={'title': {
#             'text': 'Stock Quantity'}})
#     return render(request, 'main/map.html', {'stock_chart': cht})
'''this is using highcharts'''
# def stock_chart_view(request):
#     stocks = sq.objects.all()
#     return render(request, 'main/map.html', {'stocks': stocks})

'''this is using chartjs'''

def stock_chart_view(request):
    stocks = sq.objects.all()
    print(stocks)
    return render(request, 'main/admin.html', {'stocks': stocks})

