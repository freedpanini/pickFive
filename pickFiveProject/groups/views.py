from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as login_auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import GroupRegisterForm
from .models import *
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
import datetime


def register(request):
    if request.method == 'POST':
        form = GroupRegisterForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.Admin = request.user
            group.IsActive = True
            group.UpdatedAt = datetime.date.today()
            group.CreatedAt = datetime.date.today()
            group.save()
            print("DEBUG HERE:: ",group)

            # Add initial accounts to group
            admin = GroupXAccount(Account = group.Admin, Group = group)
            admin.save()

            accounts = form.cleaned_data.get('optional_accounts')
            accounts_list = accounts.split(",")
            print("debug: ", accounts_list)
            for account in accounts_list:
                account = account.strip()
                if account == request.user.username or not account:
                    continue
                a = GroupXAccount(Account =  Account.objects.get(username = account), Group = group)
                a.save()

            messages.success(request, f'Your group has been created !')
            return redirect('index')
    else:
        form = GroupRegisterForm()
    return render(request, 'registerGroup.html', {'form': form, 'title':'register here'})