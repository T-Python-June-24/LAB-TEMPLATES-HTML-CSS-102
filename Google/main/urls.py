from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page, name='home'),
    path('terms/',views.terms_page, name='terms'),
]
