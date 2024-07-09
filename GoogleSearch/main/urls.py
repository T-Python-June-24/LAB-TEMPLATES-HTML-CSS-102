from . import views
from django.urls import path

app_name="main"
urlpatterns=[ 
    path("",views.home_view, name="home_view"),
    path("inheritance/" , views.inheritance_view , name="inheritance_view"),


]