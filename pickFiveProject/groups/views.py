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
from django.http import HttpResponseRedirect

@login_required
def group(request, group_id):
    group = Group.objects.get(GroupID = group_id)
    print("GROUP" , group)
    is_member = False

    if request.method == 'POST':
        print("POST")

        if request.POST['action'] == 'JOIN':
            a = GroupXAccount(Account =  Account.objects.get(username = request.user), Group = group)
            a.save()
            group_users = GroupXAccount.objects.filter(Group= group).select_related()
            is_member = True
            context = {'title':'index', 'group': group, 'group_users':group_users, 'is_member': is_member}
            return redirect('index')
        elif request.POST['action'] == 'LEAVE':
            AccountXGroup = GroupXAccount.objects.filter(Group= group, Account = request.user)
            AccountXGroup.delete()
            is_member = False
            group_users = GroupXAccount.objects.filter(Group= group).select_related()
            return redirect('index')

    else:
        group_users = GroupXAccount.objects.filter(Group= group).select_related()
        if GroupXAccount.objects.filter(Group= group, Account = request.user).exists():
            is_member = True

        context = {'title':'index', 'group': group, 'group_users':group_users, 'is_member': is_member}
        return render(request, 'group.html',context)

@login_required
def joinGroup(request, group_id):
    group = Group.objects.get(GroupID = group_id)
    a = GroupXAccount(Account =  Account.objects.get(username = request.user), Group = group)
    a.save()
    group_users = GroupXAccount.objects.filter(Group= group).select_related()

    context = {'title':'index', 'group': group, 'group_users':group_users, 'is_member':True}
    return render(request, 'group.html',context)

@login_required
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