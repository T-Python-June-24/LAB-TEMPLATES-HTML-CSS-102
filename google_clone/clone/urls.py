from . import views
from django.urls import path


app_name = 'clone'

urlpatterns = [
    path('', views.search, name='search'),
    path('term/', views.term, name='term'),
]
