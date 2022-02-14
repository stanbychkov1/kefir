from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=500, blank=False, null=False,
                                unique=True)
    email = models.EmailField(blank=False, null=False, unique=True)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)

    class Meta:
        ordering = ('id',)
