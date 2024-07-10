from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.
def home_view(request:HttpRequest):
    return render(request,"main/index.html")
def terms_of_services(request:HttpRequest):
    return render(request,"main/term.html")


