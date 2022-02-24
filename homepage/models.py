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
        return self.headline
