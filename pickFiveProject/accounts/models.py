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


class Group(models.Model):

    GroupID = models.AutoField(primary_key=True)  # group id, which is the primary key
    GroupName = models.CharField(max_length=30)  # group name
    AdminID = models.ForeignKey(
        Account, on_delete=models.RESTRICT  # IS THIS RIGHT?
    )  # admin id - an account id, restrict delete
    IsPublic = models.BooleanField()  # is the group public or private
    IsActive = models.BooleanField()  # is the group active or not
    CreatedAt = models.DateTimeField(auto_now_add=True)  # created time
    UpdatedAt = models.DateTimeField(auto_now=True)  # last time the group was updated

    def __str__(self):
        return "Your group name is:" + self.GroupName


class GroupXAccount(models.Model):

    GroupXAccountID = models.AutoField(
        primary_key=True
    )  # group x account id, which is the primary key
    GroupID = models.ForeignKey(
        Group, on_delete=models.CASCADE
    )  # group id - a group id, cascade delete
    AccountID = models.ForeignKey(
        Account, on_delete=models.CASCADE
    )  # account id - an account id, cascade delete

    def __str__(self):
        return "Your group x account id is:" + self.GroupXAccountID


class Teams(models.Model):

    TeamID = models.AutoField(primary_key=True)  # team id, which is the primary key
    TeamName = models.CharField(max_length=30)  # team name

    def __str__(self):
        return (
            "Your team id is:" + self.TeamID + "and the team name is:" + self.TeamName
        )


class Spreads(models.Model):

    SpreadID = models.AutoField(primary_key=True)  # spread id, which is the primary key
    FavID = models.ForeignKey(
        Teams, on_delete=models.RESTRICT
    )  # fav id - a team id, restrict delete
    DogID = models.ForeignKey(
        Teams, on_delete=models.RESTRICT
    )  # dog id - a team id, restrict delete
    PointDiff = models.DecimalField(max_digits=3, decimal_places=1)  # spread
    CreateDate = models.DateTimeField(auto_now_add=True)  # created time
    Year = models.IntegerField()  # year
    Week = models.IntegerField()  # week

    def __str__(self):
        return (
            "Your spread id is:"
            + self.SpreadID
            + "for the two teams:"
            + self.FavID
            + "and"
            + self.DogID
            + "with a spread of"
            + self.PointDiff
            + "created on"
            + self.CreateDate
            + "for the year"
            + self.Year
            + "and week"
            + self.Week
        )


class Picks(models.Model):

    PickID = models.AutoField(primary_key=True)  # pick id, which is the primary key
    GroupXAccountID = models.ForeignKey(
        GroupXAccount, on_delete=models.CASCADE
    )  # group x account id - a group x account id, cascade delete
    PickName = models.CharField(max_length=30)  # pick name
    PickText = models.TextField()  # pick text
    # PickDate = models.DateField()  # pick date
    SpreadID = models.ForeignKey(
        Spreads, on_delete=models.RESTRICT
    )  # spread id - a spread id, restrict delete

    def __str__(self):
        return "Your pick id is:" + self.PickID


class Outcomes(models.Model):

    SpreadID = models.ForeignKey(
        Spreads, on_delete=models.RESTRICT
    )  # spread id - a spread id, restrict delete
    PointDiff = models.DecimalField(max_digits=3, decimal_places=1)  # spread
    WinTeamID = models.ForeignKey(
        Teams, on_delete=models.RESTRICT
    )  # win team id - a team id, restrict delete

    def __str__(self):
        return (
            "The spread id is:"
            + self.SpreadID
            + "with a spread of"
            + self.PointDiff
            + "and the winning team id is:"
            + self.WinTeamID
        )
