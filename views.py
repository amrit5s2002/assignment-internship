from django.shortcuts import render
import pandas as pd
from django.http import JsonResponse 
from .models import *

# Create your views here.

def hello(request,*args, **kwargs):
    queryset = Sample.objects.all()
    return render(request,'hello.html',{'obj' : queryset})