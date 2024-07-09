from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

# Create your views here.
def search(request):
    return render(request, 'clone/search.html')

def term(request):
    return render(request, 'clone/term.html')