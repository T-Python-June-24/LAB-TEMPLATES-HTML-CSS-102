from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def google(HttpRequest:HttpRequest):
    
    return render(HttpRequest , 'page_google/index.html')
    