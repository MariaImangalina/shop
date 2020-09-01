from django.db import models
from django.contrib import auth

class User(auth.models.User, auth.models.PermissionsMixin):
    address = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.username
