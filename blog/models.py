from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Blog(models.Model):
    postid=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    author=models.ForeignKey(User, on_delete = models.CASCADE)
    content=models.TextField()
    date_posted=models.DateTimeField()
    likes=models.IntegerField(default=0)
    dislikes=models.IntegerField(default=0)
    reports=models.IntegerField(default=0)
    images = models.ImageField(default = 'default_blog.jpg', upload_to= 'blog/images')

    def __str__(self):
        return str(self.postid) + '-' + str(self.author) + ': ' + str(self.title)

    def get_absolute_url(self):
        return reverse('my-blogs')
