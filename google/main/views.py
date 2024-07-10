from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import random
import string

def home(request):

    return render(request, "main/home.html")

def terms(request):

    return render(request, "main/terms.html")