from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Bees(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'users/profile_pics')

    def __str__(self):
        return self.user.get_full_name()
