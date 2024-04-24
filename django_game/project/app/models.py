from django.contrib.auth.models import AbstractUser
from django.db import models


class Skin(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=30)
    price = models.IntegerField()


class User(AbstractUser):
    email = models.EmailField(unique=True)
    fio = models.CharField(max_length=55)
    skins = models.ManyToManyField(Skin)
    money = models.IntegerField(default=0)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["fio", "username"]
