from django.db import models

# Create your models here.


class Account(models.Model):

    AccountID = models.AutoField(
        primary_key=True
    )  # account id, whcih is the primary key
    Username = models.CharField(max_length=30)  # username
    Password = models.CharField(max_length=30)  # pass
    Email = models.EmailField()  # email
    CreateDate = models.DateTimeField(auto_now_add=True)  # created time
    UpdateDate = models.DateTimeField(
        auto_now=True
    )  # last time the account was updated
    BirthDate = models.DateField()  # birth date
    FirstName = models.CharField(max_length=30)  # first name
    LastName = models.CharField(max_length=30)  # last name

    def __str__(self):
        return "Hello " + self.FirstName + "your username is:" + self.Username