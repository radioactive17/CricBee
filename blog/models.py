from django.db import models
from django.utils import timezone

class Blog(models.Model):
    postid=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200,default='User')
    content=models.TextField()
    date_posted=models.DateTimeField()
    likes=models.IntegerField(default=0)
    dislikes=models.IntegerField(default=0)
    reports=models.IntegerField(default=0)

    def __str__(self):
        return self.title
