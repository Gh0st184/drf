from django.contrib.auth.models import AbstractUser
from django.db import models


class MyCustomUser(AbstractUser):
    email = models.EmailField(verbose_name='Email', unique=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.username}"
