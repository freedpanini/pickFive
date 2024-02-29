from django.db import models
from accounts.models import *
from groups.models import *
# Create your models here.

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
        Teams, on_delete=models.RESTRICT, related_name='FavID'
    )  # fav id - a team id, restrict delete
    DogID = models.ForeignKey(
        Teams, on_delete=models.RESTRICT, related_name='DogID'
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
