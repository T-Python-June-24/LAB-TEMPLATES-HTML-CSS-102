from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, 'main/home.html')

def terms_page(request):
    return render(request, 'main/terms.html')