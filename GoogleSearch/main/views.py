from django.shortcuts import render
from django.conf import settings

# Create your views here.

def home(request):
    print(settings.BASE_DIR)
    return render(request, 'main/home.html')

def terms(request):
    return render(request, 'main/terms.html')