from . import views
from django.urls import path

app_name = 'main'
urlpatterns = [
    path('', views.search_view, name='search_view'),
    path('tos/', views.tos_view, name='tos_view'),
]
