from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def google(HttpRequest:HttpRequest):
    
    return render(HttpRequest , 'page_google/Home_page.html')

def Terms_of_Service_Page(HttpRequest:HttpRequest):
    return render(HttpRequest , 'page_google/Terms_of_Service_Page.html')