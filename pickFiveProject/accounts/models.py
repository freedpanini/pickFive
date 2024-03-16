from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Account(AbstractUser):
    list_display = ('username', 'email', 'first_name', 'last_name', 'accountID')
    accountID = models.AutoField(
        primary_key=True, unique=True
    )  # account id, whcih is the primary key
    createDate = models.DateTimeField(auto_now_add=True)  # created time
    updateDate = models.DateTimeField(
        auto_now=True
    )  # last time the account was updated
