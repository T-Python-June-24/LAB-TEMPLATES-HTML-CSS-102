from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


# Create your views here.
def search_view(request):
    return render(request, 'main/search.html')


def tos_view(request):
    return render(request, 'main/tos.html')
