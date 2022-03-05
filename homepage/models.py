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
    topic = models.TextField(default = '')
    headline=models.CharField(max_length=750)
    intro = models.TextField(default = '')
    upload_time=models.CharField(max_length=50)
    link=models.TextField()
    image=models.ImageField(upload_to=None)
    news = models.TextField(default = '')

    def __str__(self):
        return str(self.newsid) + "-" + str(self.headline)

class Fixtures(models.Model):
    fixture_id = models.AutoField(primary_key = True)
    fixture_type = models.CharField(max_length = 50)
    date = models.DateField()
    tour = models.CharField(max_length = 500)
    match = models.CharField(max_length = 500)
    location = models.CharField(max_length = 500)
    time = models.CharField(max_length = 500)

    def __str__(self):
        return str(self.fixture_type) + ' - ' + str(self.date) + ':' + str(self.match)

class Fix_Date(models.Model):
    date = models.DateField()

    def __str__(self):
        return str(self.date)
