from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
