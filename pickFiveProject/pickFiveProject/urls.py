"""pickFiveProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from accounts import views as accounts_view
from groups import views as groups_view
from django.contrib.auth import views as auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('login/', accounts_view.login, name ='login'),
    path('logout/', auth.LogoutView.as_view(template_name ='index.html'), name ='logout'),
    path('register/', accounts_view.register, name ='register'),
    path('admin/', admin.site.urls),
    path('createGroup/', groups_view.register, name ='createGroup'),
    path('group/<int:group_id>', groups_view.group, name ='group')


]
