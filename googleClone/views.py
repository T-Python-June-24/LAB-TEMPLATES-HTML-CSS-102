from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'googleClone/index.html')



def terms(request):
    return render(request, 'googleClone/terms.html')
