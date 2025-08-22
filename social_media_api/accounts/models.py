from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    following = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="followers",
        blank=True
    )

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Unique name to avoid conflict
        blank=True
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Unique name to avoid conflict
        blank=True
    )

    def __str__(self):
        return self.username