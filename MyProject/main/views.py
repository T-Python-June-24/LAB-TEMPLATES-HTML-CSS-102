from django.shortcuts import render
from django.http import HttpRequest

def main_view(request:HttpRequest):

    return render(request,'main/base.html')
    

# Create your views here.
