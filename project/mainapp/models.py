from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    photo = models.CharField(verbose_name='photo url', max_length=256, null=True)


class Friend(models.Model):
    first_name = models.CharField(verbose_name='first name', max_length=32)
    last_name = models.CharField(verbose_name='last name', max_length=32)
    photo_url = models.CharField(verbose_name='photo url', max_length=256)
    domain = models.CharField(verbose_name='vk domain', max_length=16)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
