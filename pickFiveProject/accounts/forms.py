from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Account

class AccountRegisterForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ("first_name","last_name","username", "email", "password1", "password2")
