from django.forms import ModelForm
from django import forms

from .models import Group

class GroupRegisterForm(ModelForm):
    optional_accounts = forms.CharField(required=False)

    class Meta:
        model = Group
        fields = ("GroupName", "IsPublic")
