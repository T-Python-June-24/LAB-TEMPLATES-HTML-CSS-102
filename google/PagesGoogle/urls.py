from . import views
from django.urls import path

NameApps="PagesGoogle"


urlpatterns = [
    path("" , views.google , name="Google"),
    path("Terms_of_Service_Page/" , views.Terms_of_Service_Page, name="Terms_of_Service_Page")
]