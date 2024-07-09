from . import views
from django.urls import path

NameApps="PagesGoogle"


urlpatterns = [
    path("" , views.google , name="Google")
]