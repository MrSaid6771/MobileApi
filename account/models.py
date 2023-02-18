from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Clent(models.Model):
    username = models.CharField(max_length=255)
    clent_phone_number = models.CharField(unique=True, max_length=255, blank=True, null=True)
    kafil = models.CharField(max_length=255, blank=True, null=True)
    kafil_phone_number = models.CharField(default=0, max_length=255, blank=True, null=True)
    status = models.IntegerField(default=0, choices=(
        (0, 'platinum'),
        (1, 'blacklist'),
    ))
    def __str__(self):
        return self.username
