from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Bees


@receiver(post_save, sender = User)
def create_bees(sender, instance, created, **kwargs):
    if created:
        Bees.objects.create(user=instance)


@receiver(post_save, sender = User)
def save_bees(sender, instance, created, **kwargs):
    if created:
        instance.bees.save()
