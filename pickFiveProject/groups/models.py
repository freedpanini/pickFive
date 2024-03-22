from django.db import models
from accounts.models import *
# Create your models here.


class Group(models.Model):

    GroupID = models.AutoField(primary_key=True)  # group id, which is the primary key
    GroupName = models.CharField(max_length=30)  # group name
    Admin = models.ForeignKey(
        Account, on_delete=models.RESTRICT  # IS THIS RIGHT?
    )  # admin id - an account id, restrict delete
    IsPublic = models.BooleanField()  # is the group public or private
    IsActive = models.BooleanField()  # is the group active or not
    CreatedAt = models.DateTimeField(auto_now_add=True)  # created time
    UpdatedAt = models.DateTimeField(auto_now=True)  # last time the group was updated

    def __str__(self):
        return "Your group name is:" + self.GroupName + " ID: " + str(self.GroupID)


class GroupXAccount(models.Model):

    GroupXAccountID = models.AutoField(
        primary_key=True
    )  # group x account id, which is the primary key
    Group = models.ForeignKey(
        Group, on_delete=models.CASCADE
    )  # group id - a group id, cascade delete
    Account = models.ForeignKey(
        Account, on_delete=models.CASCADE
    )  # account id - an account id, cascade delete

    def __str__(self):
        return "Your group x account id is:" + str(self.GroupXAccountID)