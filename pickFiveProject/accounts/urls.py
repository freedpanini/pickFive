from django.urls import path
from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_view
from django.contrib.auth import views as auth
from . import views

urlpatterns = [
path('', views.index, name ='index'),
]