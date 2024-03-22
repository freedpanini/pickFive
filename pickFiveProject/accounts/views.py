from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as login_auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import AccountRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from groups.models import *
  
  
#################### index####################################### 
def index(request):
    available_groups = Group.objects.filter(IsPublic = True, IsActive = True)
    user_groups = GroupXAccount.objects.filter(Account= request.user).select_related()
    print("user", request.user)

    print("GROUPS", available_groups)
    print("USEr GROUPS", user_groups)

    context = {'title':'index', 'available_groups': available_groups, 'user_groups':user_groups}
    return render(request, 'index.html',context)
  
########### register here ##################################### 
def register(request):
    if request.method == 'POST':
        form = AccountRegisterForm(request.POST)
        if form.is_valid():
            account = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = AccountRegisterForm()
    return render(request, 'register.html', {'form': form, 'title':'register here'})
  
################ login forms################################################### 
def login(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login_auth(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form, 'title':'log in'})