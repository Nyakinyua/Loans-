from django.shortcuts import render
from .models import *
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
# Create your views here.


def index(request):
    all_customers = Customer.get_customers()
    return render(request,"index.html",{"customers":all_customers})

 
