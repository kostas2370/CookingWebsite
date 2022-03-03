from django.urls import path
from . import views

urlpatterns = [
    path('', views.ask1,name="home"),
    path('about/', views.ask2,name="home"),
]