from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator

class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[UnicodeUsernameValidator()],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(
        Group,
        related_name='myauth_user_groups',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='myauth_user_permissions',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
    )