from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User

class Bees(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.user.get_full_name()

class Recentnews(models.Model):
    newsid=models.AutoField(primary_key=True)
    headline=models.CharField(max_length=750)
    upload_time=models.CharField(max_length=50)
    link=models.TextField()
    image=models.ImageField(upload_to=None)

    def __str__(self):
        return self.headline

class MatchDetails(models.Model):
    #Details about match
    matchid=models.IntegerField(primary_key=True)
    srs=models.CharField(max_length=1000)
    mnum=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    mchstate=models.CharField(max_length=100)
    status=models.TextField()
    venue_name=models.TextField()
    venue_location=models.TextField()
    toss=models.CharField(max_length=1000)
    date_modified_md=models.DateTimeField('MatchDetails Modified on')

class TeamDetails(models.Model):
    #Details about team in a match
    matchid=models.ForeignKey('MatchDetails',on_delete=models.CASCADE)
    team_name1=models.CharField(max_length=100)
    runs1=models.CharField(max_length=100)
    wickets1=models.CharField(max_length=12)
    overs1=models.CharField(max_length=100)
    inning_num1=models.CharField(max_length=4,default='1')

    team_name2=models.CharField(max_length=100)
    runs2=models.CharField(max_length=100,default=None)
    wickets2=models.CharField(max_length=12,default=None)
    overs2=models.CharField(max_length=100,default=None)
    inning_num2=models.CharField(max_length=4,default='2')

    team_name3=models.CharField(max_length=100)
    runs3=models.CharField(max_length=100,default=None)
    wickets3=models.CharField(max_length=12,default=None)
    overs3=models.CharField(max_length=100,default=None)
    inning_num3=models.CharField(max_length=4,default='3')

    team_name4=models.CharField(max_length=100)
    runs4=models.CharField(max_length=100,default=None)
    wickets4=models.CharField(max_length=12,default=None)
    overs4=models.CharField(max_length=100,default=None)
    inning_num4=models.CharField(max_length=4,default='3')

    date_modified_td=models.DateTimeField('TeamDetails Modified on')
